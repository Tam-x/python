#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/07/19
Last edited: 2018/07/20
'''

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QFileDialog, QDialog, QHeaderView, QMessageBox
from PyQt5.QtGui import QStandardItem , QStandardItemModel
import paho.mqtt.client as mqtt
from UI.UI import Ui_MainWindow
from UI.Dialog import AboutDialog
from Icon import Icon
from Config import Config
import threading, time, queue, json, webbrowser


class WindowController(Ui_MainWindow, QDialog):
    def __init__(self, widge):
        super(WindowController, self).__init__()
        self.setupUi(widge)
        self.init(widge)

    def init(self, widge):
        self.isRunning = False
        self.firstConnection = True
        self.linkNum = -1
        self.appNum = -1
        self.current_acctive_linkid = -1
        self.socket_links_info = None
        self.socket_apps_info = None
        self.current_sys_ip = None
        self.logs = queue.Queue()
        self.timer = QTimer()
        self.remoteClient = mqtt.Client()
        self.isSysRunning = False
        self.sysInfoComing = False
        self.sysClient = mqtt.Client()
        self.actionImportCfg.triggered.connect(self.open_file)
        self.actionVisitUs.triggered.connect(self.visit_us)
        self.actionCleanLog.triggered.connect(self.clean_log)
        self.actionSoftInfo.triggered.connect(self.about_dialog)
        self.actionCmdHelp.triggered.connect(self.cmd_help)
        self.btnCurrentConnection.clicked.connect(self.click_btn_current_links)
        self.btnActivateConnection.clicked.connect(self.click_btn_activate_connection)
        self.btnList.clicked.connect(self.click_btn_app_list)
        self.btnRun.clicked.connect(self.click_btn_app_run)
        self.btnStop.clicked.connect(self.click_btn_app_stop)
        self.btnDelete.clicked.connect(self.click_btn_app_delete)
        self.btnDownLoad.clicked.connect(self.click_btn_app_ota)
        self.timer.timeout.connect(self.refrush_ui)
        self.timer.start(1)
        self.pushButton.clicked.connect(self.click_btn_syscheck)
        self.creatTable(Config.TASK_VALUE)
        self.write_sys_info()
        self.set_close(widge)

    def set_close(self, widge):
        widge.set_close(self.close_mqtt)

    def close_mqtt(self):
        self.sysClient.disconnect()
        self.remoteClient.disconnect()

    def click_btn_current_links(self):
        if self.isRunning:
            self.request_links()
        else:
            self.isRunning = True
            self.start_dthing_remote_client()

    def click_btn_activate_connection(self):
        self.activate_one_link()

    def click_btn_app_list(self):
        if int(self.current_acctive_linkid) > -1:
            self.request_list()

    def click_btn_app_run(self):
        appid = self.textRunNum.text()
        if appid and self.socket_apps_info and self.socket_apps_info.get(appid):
            self.request_run(appid)

    def click_btn_app_stop(self):
        appid = self.textStopNum.text()
        if appid and self.socket_apps_info and self.socket_apps_info.get(appid):
            self.request_stop(appid)

    def click_btn_app_delete(self):
        appid = self.textDeleteNum.text()
        if appid and self.socket_apps_info and self.socket_apps_info.get(appid):
            self.request_delete(appid)

    def click_btn_app_ota(self):
        url = self.textDownloadUrl.toPlainText()
        if url and int(self.current_acctive_linkid) > -1:
            self.request_ota(url)

    #当前dtu连接数
    def request_links(self):
        self.publish(self.get_cmd_links())

    #激活某个连接
    def activate_one_link(self):
        socketID = self.textActivateConnectionNum.text()
        if socketID and self.socket_links_info:
            if self.socket_links_info.get(socketID):
                if self.current_acctive_linkid == socketID:
                    return
                self.current_acctive_linkid = socketID
                self.socket_apps_info = None
                self.logs.put(self.socket_links_info.get(socketID)+'连接被激活')
                self.textCurrentConnection.setText(self.socket_links_info.get(socketID))
                self.appNum = 0
            else:
                self.logs.put('\n'+'连接激活失败')

    #获取app列表
    def request_list(self):
        self.publish(self.get_cmd_list())

    #运行app
    def request_run(self, appid):
        self.publish(self.get_cmd_run(appid))

    #结束app
    def request_stop(self, appid):
        self.publish(self.get_cmd_stop(appid))

    #删除app
    def request_delete(self, appid):
        self.publish(self.get_cmd_delete(appid))

    #下载app
    def request_ota(self, url):
        self.publish(self.get_cmd_ota(url))

    #启动远程控制服务
    def start_dthing_remote_client(self):
        thread = threading.Thread(target=self.client_mqtt_loop, args=(Config.CODE_MQTT_REMOTE,))
        thread.start()

    #启动设备信息服务
    def start_monitor_sys_client(self):
        thread = threading.Thread(target=self.client_mqtt_loop, args=(Config.CODE_MQTT_MONITOR,))
        thread.start()

    def client_mqtt_loop(self, code):
        client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        if(code == Config.CODE_MQTT_REMOTE):
            self.remoteClient = mqtt.Client(Config.MQTT_CLIENT + '-remote-' + client_id)
            self.remoteClient.username_pw_set(Config.MQTT_REMOTE_USER, Config.MQTT_REMOTE_PWD)
            self.remoteClient.on_connect = self.on_connect_remote
            self.remoteClient.on_message = self.on_message_remote
            try:
                self.remoteClient.connect(Config.MQTT_REMOTE_BROKER, int(Config.MQTT_REMOTE_PORT), 60)
                self.logs.put('设备上线中...')
                self.remoteClient.loop_forever()
            except:
                self.logs.put('连接失败...')
                self.isRunning = False
        else:
            self.sysClient = mqtt.Client(Config.MQTT_CLIENT + '-sys-' + client_id)
            self.sysClient.username_pw_set(Config.MQTT_MONITOR_USER, Config.MQTT_MONITOR_PWD)
            self.sysClient.on_connect = self.on_connect_sys
            self.sysClient.on_message = self.on_message_sys
            self.sysClient.connect(Config.MQTT_MONITOR_BROKER, int(Config.MQTT_MONITOR_PORT), 60)
            self.sysClient.loop_forever()

    def on_connect_remote(self, client, userdata, flags, rc):
        print("Connected remote with result code " + str(rc))
        client.subscribe(Config.MQTT_TOPIC_REMOTE_TO_CLIENT)
        if self.firstConnection:
            self.firstConnection = False
            self.request_links()

    def on_message_remote(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode("utf-8"))
        self.handle_remote_msg(msg.payload.decode("utf-8"))

    def on_connect_sys(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        print(Config.MQTT_TOPIC_CLIENT_TO_MONITOR % (self.current_sys_ip))
        client.subscribe(Config.MQTT_TOPIC_CLIENT_TO_MONITOR % (self.current_sys_ip))

    def on_message_sys(self, client, userdata, msg):
        print(msg.topic + " cc" )
        from Parser.Parser import TlvParser
        t = TlvParser()
        a, b = t.checkFrame(msg.payload)
        # Config.SYS_VALUE = {11: '-', 12: '-', 13: '-', 14: '-', 15: '-', 16: '-', 17: '-', 18: '-', 51: '-', 52: '-'}
        Config.TASK_VALUE = {}
        t.parse_tlv(b, 0)
        self.sysInfoComing = True


    def handle_remote_msg(self, jsonMsg):
        msg = json.loads(jsonMsg)
        socket = msg.get('current_tcp_socket')
        socketId = msg.get('current_tcp_id')
        cmd = msg.get('cmd')
        cmdStatus = msg.get('cmd_status')
        body = msg.get('body')
        infos = json.loads(body)
        print(infos)
        if(cmd.lower() == Config.CMD_STR_LINKS):
            self.logs.put('\n'+'当前连接'+'\n-----------------------------------')
            self.linkNum = 0
            if infos:
                self.socket_links_info = infos
                for key, value in self.socket_links_info.items():
                    self.logs.put('id：'+key+",client："+value)
                    self.linkNum += 1
                if not self.socket_links_info.get(self.current_acctive_linkid):
                    self.current_acctive_linkid = -1
                    self.socket_apps_info = None
                    self.appNum = 0
            else:
                self.linkNum = 0
                self.appNum = 0
                self.current_acctive_linkid = -1
                self.socket_links_info = None
                self.socket_apps_info = None
                self.logs.put('没有客户接入!')
        elif(cmd.lower() == Config.CMD_STR_LIST):
            self.appNum = 0
            if infos:
                self.logs.put('\n' + '当前应用' + '\n-----------------------------------')
                self.socket_apps_info = infos
                for key, value in  infos.items():
                    self.logs.put('id：'+key+",app："+value)
                    self.appNum += 1
            else:
                self.logs.put('没有应用!')
        elif(cmd.lower() == Config.CMD_STR_RUN):
            self.logs.put('\n' + '运行应用：' + cmdStatus)
        elif(cmd.lower() == Config.CMD_STR_DESTROY):
            self.logs.put('\n' + '停止应用：' + cmdStatus)
        elif (cmd.lower() == Config.CMD_STR_DELE):
            self.logs.put('\n' + '删除应用：' + cmdStatus)
        elif (cmd.lower() == Config.CMD_STR_OTA):
            self.logs.put('\n' + '下载应用：' + cmdStatus)
        else:
            pass

    def get_cmd_links(self):
        cmd = {Config.KEY_CMD:Config.CMD_STR_LINKS,
               Config.KEY_CMD_DIRCTION:Config.CMD_STR_DIRCTION_DOWN,
               Config.KEY_LINK_ID:'',
               Config.KEY_CMD_PARAM:''}
        return json.dumps(cmd)

    def get_cmd_list(self):
        cmd = {Config.KEY_CMD:Config.CMD_STR_LIST,
               Config.KEY_CMD_DIRCTION:Config.CMD_STR_DIRCTION_DOWN,
               Config.KEY_LINK_ID:int(self.current_acctive_linkid),
               Config.KEY_CMD_PARAM:''}
        return json.dumps(cmd)

    def get_cmd_run(self, appid):
        cmd = {Config.KEY_CMD:Config.CMD_STR_RUN,
               Config.KEY_CMD_DIRCTION:Config.CMD_STR_DIRCTION_DOWN,
               Config.KEY_LINK_ID:int(self.current_acctive_linkid),
               Config.KEY_CMD_PARAM:int(appid)}
        return json.dumps(cmd)

    def get_cmd_stop(self, appid):
        cmd = {Config.KEY_CMD: Config.CMD_STR_DESTROY,
               Config.KEY_CMD_DIRCTION: Config.CMD_STR_DIRCTION_DOWN,
               Config.KEY_LINK_ID: int(self.current_acctive_linkid),
               Config.KEY_CMD_PARAM: int(appid)}
        return json.dumps(cmd)

    def get_cmd_delete(self, appid):
        cmd = {Config.KEY_CMD: Config.CMD_STR_DELE,
               Config.KEY_CMD_DIRCTION: Config.CMD_STR_DIRCTION_DOWN,
               Config.KEY_LINK_ID: int(self.current_acctive_linkid),
               Config.KEY_CMD_PARAM: int(appid)}
        return json.dumps(cmd)

    def get_cmd_ota(self, url):
        cmd = {Config.KEY_CMD: Config.CMD_STR_OTA,
               Config.KEY_CMD_DIRCTION: Config.CMD_STR_DIRCTION_DOWN,
               Config.KEY_LINK_ID: int(self.current_acctive_linkid),
               Config.KEY_CMD_PARAM: url}
        return json.dumps(cmd)

    def publish(self, cmd):
        self.remoteClient.publish(Config.MQTT_TOPIC_CLIENT_TO_REMOTE, cmd)

    def cmd_help(self):
        help = '''\n命令菜单：
        \n-----------------------------------------
        \n当前连接  ---------------  查看所有接入设备
        \n激活连接  ---------------  连接某个接入设备
        \n应用列表  ---------------  查看接入设备应用
        \n运行应用  ---------------  运行应用 + ID
        \n停止应用  ---------------  停止应用 + ID
        \n删除应用  ---------------  删除应用 + ID
        \n远程下载  ---------------  设备远程下载应用
        '''
        self.textBrowser.append(help)

    def refrush_ui(self):
        while self.logs.qsize()>0:
            self.textBrowser.append(self.logs.get())

        if self.linkNum > -1:
            self.textCurrentConnectionNum.setText(str(self.linkNum))
            if self.linkNum == 0 or int(self.current_acctive_linkid) == -1:
                self.textCurrentConnection.setText('当前没有连接被激活')
            self.linkNum = -1

        if self.appNum > -1:
            self.textListNum.setText(str(self.appNum))
            if self.appNum == 0:
                self.socket_apps_info = None
            self.appNum = -1

        if self.sysInfoComing:
            self.creatTable(Config.TASK_VALUE)
            self.write_sys_info()
            self.sysInfoComing = False

    def visit_us(self):
        webbrowser.open("http://www.yarlungsoft.com")
        pass

    def clean_log(self):
        self.textBrowser.clear()

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(caption='选择配置文件')
        importCfg = False
        if fileName:
            try:
                for line in open(fileName[0]):
                    if '#' not in line and line.strip():
                        if 'supplier' in line:
                            Config.MQTT_CLIENT = line.split(':')[1].strip()
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_broker' in line:
                            Config.MQTT_REMOTE_BROKER = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_port' in line:
                            Config.MQTT_REMOTE_PORT = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_user' in line:
                            Config.MQTT_REMOTE_USER = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_pwd' in line:
                            Config.MQTT_REMOTE_PWD = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_topic'in line:
                            self.topic = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_sys_broker' in line:
                            Config.MQTT_MONITOR_BROKER = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_sys_port' in line:
                            Config.MQTT_MONITOR_PORT = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_sys_user' in line:
                            Config.MQTT_MONITOR_USER = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_sys_pwd' in line:
                            Config.MQTT_MONITOR_PWD = line.split(':')[1].strip().replace("\n", "")
                            importCfg = True
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_sys_topic' in line:
                            pass
                    #TODO 导入配置文件，重新连接
                    if importCfg:
                        self.isRunning = False
                        try:
                            self.remoteClient.disconnect()
                        except:
                            pass
            except:
                self.textBrowser.setText("操作失败...")

    def about_dialog(self):
        dialog = AboutDialog()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            return True
        return False

    def click_btn_syscheck(self):
        if not self.is_right_ip():
            QMessageBox.warning(None, '提示', '没有输入正确的设备地址！', QMessageBox.Ok)
            return
        self.current_sys_ip = self.lineEdit.text()+'.'\
                              + self.lineEdit_2.text()+'.'\
                              + self.lineEdit_3.text()+'.'\
                              + self.lineEdit_4.text()
        if self.isSysRunning:
            self.pushButton.setText('查 看')
            self.isSysRunning = False
            Config.SYS_VALUE = {11: '-', 12: '-', 13: '-', 14: '-', 15: '-', 16: '-', 17: '-', 18: '-', 51: '-', 52: '-'}
            Config.TASK_VALUE = {}
            self.sysInfoComing = True
            try:
                self.sysClient.disconnect()
            except:
                pass
        else:
            try:
                self.isSysRunning = True
                self.pushButton.setText('停 止')
                self.start_monitor_sys_client()
            except:
                self.isSysRunning = False
                self.pushButton.setText('查 看')

    def is_right_ip(self):
        if not self.lineEdit.text():
            return False
        if not self.lineEdit_2.text():
            return False
        if not self.lineEdit_3.text():
            return False
        if not self.lineEdit_4.text():
            return False
        return True

    def write_sys_info(self):
        self.textMemoryStatus.setText(Config.SYS_VALUE.get(11))
        self.textOutmemoryStatus.setText(Config.SYS_VALUE.get(12))
        if(Config.SYS_VALUE.get(13) == '-'):
            self.textCpuUsedRate.setText(Config.SYS_VALUE.get(13))
        else:
            self.textCpuUsedRate.setText(Config.SYS_VALUE.get(13) + ' %')
        if Config.SYS_VALUE.get(14) == '-':
            self.textCpuTemp.setText(Config.SYS_VALUE.get(14))
        else:
            self.textCpuTemp.setText(Config.SYS_VALUE.get(14) + ' ℃')
        if Config.SYS_VALUE.get(15) == '-':
            self.textCpuVoletage.setText(Config.SYS_VALUE.get(15))
        else:
            self.textCpuVoletage.setText(Config.SYS_VALUE.get(15) + ' V')
        if Config.SYS_VALUE.get(16) == '-':
            self.textUsedMemoryRate.setText(Config.SYS_VALUE.get(16))
        else:
            self.textUsedMemoryRate.setText(Config.SYS_VALUE.get(16) + ' %')
        self.textUsedMemory.setText(Config.SYS_VALUE.get(17))
        self.textUnUsedMemory.setText(Config.SYS_VALUE.get(18))
        self.textGpsJ.setText(Config.SYS_VALUE.get(51))
        self.textGpsW.setText(Config.SYS_VALUE.get(52))



    def creatTable(self, datas):
        if datas:
            rows = datas.keys()
            rows = (list(rows))
            rows.sort()
            row = len(rows)
            self.model = QStandardItemModel(row, 5)
            print(datas)
            print(row)
            for m in range(row):
                for column in range(5):
                    if column == 0:
                        if datas.get(rows[m]).get(31):
                            item = QStandardItem(str(rows[m]))
                        else:
                            item = QStandardItem('-')
                        item.setEnabled(False)
                    elif column == 1:
                        if datas.get(rows[m]).get(32):
                            item = QStandardItem(datas.get(rows[m]).get(32))
                        else:
                            item = QStandardItem('-')
                        item.setEnabled(False)
                    elif column == 2:
                        if datas.get(rows[m]).get(33):
                            item = QStandardItem(datas.get(rows[m]).get(33))
                        else:
                            item = QStandardItem('-')
                        item.setEnabled(False)
                    elif column == 3:
                        if datas.get(rows[m]).get(34):
                            item = QStandardItem(datas.get(rows[m]).get(34))
                        else:
                            item = QStandardItem('-')
                        item.setEnabled(False)
                    else:
                        if datas.get(rows[m]).get(35):
                            item = QStandardItem(datas.get(rows[m]).get(35))
                        else:
                            item = QStandardItem('-')
                        item.setEnabled(False)
                    item.setTextAlignment(Qt.AlignCenter)
                    self.model.setItem(m, column, item)
        else:
            self.model = QStandardItemModel(0, 5)
        self.model.setHorizontalHeaderLabels(['进程编号', '使用内存', '未使用内存', '最大使用内存', '内存使用率(%)'])
        self.tableWidget.setModel(self.model)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

