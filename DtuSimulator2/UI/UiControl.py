#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/07/10
Last edited: 2018/07/13
'''

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QFileDialog, QDialog
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
from UI.UI import Ui_MainWindow
from TLV.SamrtWater2 import SmartWater
from TLV.SECS import Secs
from TLV.TlvData import TlvData
from TLV import TlvHelper
from Config.Config import Config
from UI.Dialog import AboutDialog
import threading, time, queue
import inspect, webbrowser, ctypes, random


class windowController(Ui_MainWindow, QDialog):
    def __init__(self, widge):
        super(windowController, self).__init__()
        self.setupUi(widge)
        self.init()

    def init(self):
        self.isStart = False
        self.count = 0
        self.topic = None
        self.threadEvent = threading.Event()
        self.msgQueue = queue.Queue()
        self.timer = QTimer()
        self.threads = []
        self.comboProject.qLineEdit.setText('选择项目')
        self.comboProject.set_items(Config.PROJECTS)
        self.action_import.triggered.connect(self.open_file)
        self.action_3.triggered.connect(self.visit_us)
        self.action_4.triggered.connect(self.clean_log)
        self.action.triggered.connect(self.aboutDialog)
        self.comboProject.currentTextChanged.connect(self.set_pcomm_default_title)
        self.comboData.currentTextChanged.connect(self.set_dcomm_default_title)
        self.btnStart.clicked.connect(self.start)
        self.timer.timeout.connect(self.refrush_ui)

        for i in range(1, self.comboProject.row_num):
            self.comboProject.qCheckBox[i].stateChanged.connect(self.update_dcomm_value)

    def visit_us(self):
        webbrowser.open("http://www.yarlungsoft.com")
        pass

    def clean_log(self):
        self.textBrowser.clear()

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(caption='选择DTU模拟器配置文件')
        if fileName:
            try:
                for line in open(fileName[0]):
                    if '#' not in line and line.strip():
                        if 'supplier' in line:
                            Config.TOPIC_L2_DEFAULT = line.split(':')[1].strip()
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_broker' in line:
                            Config.BROKER = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_user' in line:
                            Config.USER = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'mqtt_pwd' in line:
                            Config.PWD = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        elif 'super_topic'in line:
                            self.topic = line.split(':')[1].strip().replace("\n", "")
                            self.textBrowser.append(line.strip().replace("\n", ""))
                        else:
                            pass
            except:
                self.textBrowser.setText("操作失败...")
                self.addrs = []

    def aboutDialog(self):
        dialog = AboutDialog()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            return True
        return False

    def refrush_ui(self):
        while self.msgQueue.qsize()>0:
            self.textBrowser.append(self.msgQueue.get())

    def update_dcomm_value(self):
        data = []
        list1 = list(self.comboProject.Selectlist())
        for i in list1:
            data.extend(Config.DATA_MAP.get(i))
        self.comboData.set_items(data)
        self.comboData.setCurrentText('选择数据')

    def set_pcomm_default_title(self):
        self.comboProject.setCurrentText('选择项目')

    def set_dcomm_default_title(self):
        self.comboData.setCurrentText('选择数据')

    def get_publish_datas(self, ip):
        datas = list(self.comboData.Selectlist())
        pumpTitles = []
        secsTitles = []
        electricTitles = []
        values = []
        if datas:
            for value in datas:
                if '1' in value:
                    pumpTitles.append(value)
                elif '2' in value:
                    secsTitles.append(value)
                elif '3' in value:
                    electricTitles.append(value)
            tlv = TlvData()
            if pumpTitles:
                instance = SmartWater()
                pumpDatas, wmeterDatas = instance.create_smartwater_data(pumpTitles,self.get_dtu_excep())
                if pumpDatas:
                    pumpDatas = [tlv.create_tlv_data(Config.MESSAGE_PUMP_HOUSE,ip,pumpDatas),Config.TOPIC_BASE%(Config.TOPIC_L1_SWATER, Config.TOPIC_L2_DEFAULT)]
                    values.append(pumpDatas)
                if wmeterDatas:
                    wmeterDatas = [tlv.create_tlv_data(Config.MESSAGE_METER_WATER, ip, wmeterDatas),Config.TOPIC_BASE%(Config.TOPIC_L1_SWATER, Config.TOPIC_L2_DEFAULT)]
                    values.append(wmeterDatas)
            if secsTitles:
                instance = Secs()
                secsDatas = instance.create_secs_data(secsTitles, self.get_dtu_excep())
                if secsDatas:
                    secsDatas = [tlv.create_tlv_data(Config.MESSAGE_METER_WATER, ip, secsDatas),Config.TOPIC_BASE%(Config.TOPIC_L1_SECS, Config.TOPIC_L2_DEFAULT)]
                    values.append(secsDatas)
            if electricTitles:
                pass
        return values

    def start(self):
        if list(self.comboData.Selectlist()):
            self.click_btnstart_status()
            if self.isStart:
                self.threadEvent.clear()
                for i in range(self.get_dtu_num()):
                    data = self.get_publish_datas(i)
                    thread = threading.Thread(target=self.publish_data, args=(i, data,self.threadEvent))
                    self.threads.append(thread)
                    thread.start()

    def click_btnstart_status(self):
        if self.isStart:
            self.isStart = False
            self.threadEvent.set()
            self.msgQueue.queue.clear()
            # for th in self.threads:
            #     self.stop_thread(th)
            self.threads = []
            self.btnStart.setText('启动')
        else:
            self.isStart = True
            self.threadEvent.clear()
            if not self.timer.isActive():
                self.timer.start(0.5)
            self.btnStart.setText('停止')

    def get_dtu_num(self):
        if self.rdoNumLess.isChecked():
            return random.randint(2, 5)
        elif self.rdoNumNormal.isChecked():
            return random.randint(20, 50)
        elif self.rdoNumMuch.isChecked():
            return random.randint(100, 300)

    def get_dtu_stable(self):
        if self.rdoRestady.isChecked():
            return random.randint(1, 5) > 3
        elif self.rdoNormal.isChecked():
            return random.randint(1, 100) > 3
        elif self.rdoStady.isChecked():
            return random.randint(1, 1000) > 2

    def get_dtu_excep(self):
        if self.rdoHighExcep.isChecked():
            return random.randint(1, 5) < 3
        elif self.rdoNormalExcep.isChecked():
            return random.randint(1, 100) < 3
        elif self.rdoLessExcep.isChecked():
            return random.randint(1, 1000) < 2

    def publish_data(self, ip, datas, event):
        if datas:
            id = TlvHelper.int_2_ip(ip)
            client_id = str(id)+'-'+str(time.time())
            client = mqtt.Client(client_id=client_id)
            user = Config.USER
            password = Config.PWD
            client.username_pw_set(user, password)
            try:
                client.connect(Config.BROKER)
            except:
                self.msgQueue.put(id + '未能成功连接服务器：' + Config.BROKER)
                return
            client.loop_start()
            while self.isStart:
                if self.get_dtu_stable():
                    for data in datas:
                        payload = data[0]
                        if self.topic:
                            topic = self.topic %(id)
                        else:
                            topic = data[1]+id+'/devices'
                        print(topic)
                        print(Config.BROKER)
                        client.publish(topic,bytearray(payload))
                        time.sleep(0.01)
                        if self.isStart:
                            self.msgQueue.put(id + '['+topic + ']发送消息成功'+str(data[0]))

                else:
                    self.msgQueue.put(id + '不稳定，未能成功发送数据')


                    # i = 0
                    # for data in datas:
                    #     try:
                    #         # Config.BROKER = '182.61.25.208'
                    #         id = TlvHelper.int_2_ip(ip)
                    #         publish.single("dtu/up/phouse/0.0.1.250/deivces", bytearray(data), hostname=Config.BROKER, client_id = id+'-'+str(i))
                    #         if self.isStart:
                    #             self.msgQueue.put(id + '发送消息成功['+str(data)+']')
                    #         i += 0
                    #         time.sleep(0.1)
                    #     except:
                    #         if self.isStart:
                    #             self.msgQueue.put(id+':消息发送失败'+str(data))
                print('awitt----------------------')
                if self.isStart:
                    event.wait(60)
                print('allive................')
            client.loop_stop()
            client.disconnect()
            print('over................')

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self, thread):
        try:
            self._async_raise(thread.ident, SystemExit)
        except:
            print(thread.ident)