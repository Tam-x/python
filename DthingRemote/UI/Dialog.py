#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/07/19
Last edited: 2018/07/19
'''

from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QLabel
from Config import Config

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.resize(350, 180)
        self.setWindowTitle('关于')
        self.setWindowIcon((QtGui.QIcon(':about.ico')))
        label=QLabel('版本：'+ Config.VERSION, self)
        label.move(25, 30)
        label=QLabel('名称：Dthing远程桌面工具', self)
        label.move(25, 60)
        label=QLabel('编译环境：windows8 64位', self)
        label.move(25, 90)
        label=QLabel('版权@2017-2018成都雅鲁科技所有', self)
        label.move(25, 120)