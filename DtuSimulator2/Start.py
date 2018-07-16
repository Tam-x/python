#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/07/10
Last edited: 2018/07/10
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.UiControl import windowController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = windowController(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    pass