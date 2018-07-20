#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/07/19
Last edited: 2018/07/20
'''

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog, QDialog
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
        self.init()

    def init(self):
        self.isRunning = False
        self.firstConnection = True
        self.linkNum = -1
        self.appNum = -1
        self.current_acctive_linkid = -1
        self.socket_links_info = None
        self.socket_apps_info = None
        self.logs = queue.Queue()
        self.timer = QTimer()
        self.remoteClient = mqtt.Client()
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

    def client_mqtt_loop(self, code):
        client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        if(code == Config.CODE_MQTT_REMOTE):
            self.remoteClient = mqtt.Client(Config.MQTT_CLIENT + '-' + client_id)
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
            pass


    def on_connect_remote(self, client, userdata, flags, rc):
        print("Connected remote with result code " + str(rc))
        client.subscribe(Config.MQTT_TOPIC_REMOTE_TO_CLIENT)
        if self.firstConnection:
            self.firstConnection = False
            self.request_links()

    def on_message_remote(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode("utf-8"))
        self.handle_remote_msg(msg.payload.decode("utf-8"))

    def on_connect_monitor(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(Config.MQTT_TOPIC_REMOTE_TO_CLIENT)

    def on_message_monitor(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode("utf-8"))

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

    def visit_us(self):
        webbrowser.open("http://www.yarlungsoft.com")
        pass

    def clean_log(self):
        self.textBrowser.clear()

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(caption='选择配置文件')
        if fileName:
            try:
                for line in open(fileName[0]):
                    if '#' not in line and line.strip():
                        if 'supplier' in line:
                            Config.MQTT_CLIENT = line.split(':')[1].strip()
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_broker' in line:
                            Config.MQTT_REMOTE_BROKER = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_port' in line:
                            Config.MQTT_REMOTE_PORT = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_user' in line:
                            Config.MQTT_REMOTE_USER = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote_pwd' in line:
                            Config.MQTT_REMOTE_PWD = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_remote'in line:
                            self.topic = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        else:
                            pass
                    #TODO 导入配置文件，重新连接
                    # if 9:
                    #     self.isRunning = False
                    #     try:
                    #         self.remoteClient.disconnect()
                    #     except:
                    #         pass
            except:
                self.textBrowser.setText("操作失败...")

    def about_dialog(self):
        dialog = AboutDialog()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            return True
        return False

