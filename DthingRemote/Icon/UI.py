# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dthing_remote.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnCurrentConnection = QtWidgets.QPushButton(self.centralwidget)
        self.btnCurrentConnection.setObjectName("btnCurrentConnection")
        self.horizontalLayout_7.addWidget(self.btnCurrentConnection)
        self.textCurrentConnectionNum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textCurrentConnectionNum.sizePolicy().hasHeightForWidth())
        self.textCurrentConnectionNum.setSizePolicy(sizePolicy)
        self.textCurrentConnectionNum.setMinimumSize(QtCore.QSize(25, 25))
        self.textCurrentConnectionNum.setMaximumSize(QtCore.QSize(25, 25))
        self.textCurrentConnectionNum.setFrame(False)
        self.textCurrentConnectionNum.setAlignment(QtCore.Qt.AlignCenter)
        self.textCurrentConnectionNum.setReadOnly(True)
        self.textCurrentConnectionNum.setObjectName("textCurrentConnectionNum")
        self.horizontalLayout_7.addWidget(self.textCurrentConnectionNum)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(450, 250))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 2, 7, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.textElec = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textElec.sizePolicy().hasHeightForWidth())
        self.textElec.setSizePolicy(sizePolicy)
        self.textElec.setMinimumSize(QtCore.QSize(75, 25))
        self.textElec.setMaximumSize(QtCore.QSize(75, 25))
        self.textElec.setFrame(False)
        self.textElec.setReadOnly(True)
        self.textElec.setObjectName("textElec")
        self.horizontalLayout_5.addWidget(self.textElec)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.textTemp = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textTemp.sizePolicy().hasHeightForWidth())
        self.textTemp.setSizePolicy(sizePolicy)
        self.textTemp.setMinimumSize(QtCore.QSize(75, 25))
        self.textTemp.setMaximumSize(QtCore.QSize(75, 25))
        self.textTemp.setFrame(False)
        self.textTemp.setReadOnly(True)
        self.textTemp.setObjectName("textTemp")
        self.horizontalLayout_12.addWidget(self.textTemp)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.textMemory = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textMemory.sizePolicy().hasHeightForWidth())
        self.textMemory.setSizePolicy(sizePolicy)
        self.textMemory.setMinimumSize(QtCore.QSize(75, 25))
        self.textMemory.setMaximumSize(QtCore.QSize(75, 25))
        self.textMemory.setFrame(False)
        self.textMemory.setReadOnly(True)
        self.textMemory.setObjectName("textMemory")
        self.horizontalLayout_6.addWidget(self.textMemory)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.textStorage = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textStorage.sizePolicy().hasHeightForWidth())
        self.textStorage.setSizePolicy(sizePolicy)
        self.textStorage.setMinimumSize(QtCore.QSize(75, 25))
        self.textStorage.setMaximumSize(QtCore.QSize(75, 25))
        self.textStorage.setFrame(False)
        self.textStorage.setReadOnly(True)
        self.textStorage.setObjectName("textStorage")
        self.horizontalLayout_9.addWidget(self.textStorage)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.textInnerMonitor = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textInnerMonitor.sizePolicy().hasHeightForWidth())
        self.textInnerMonitor.setSizePolicy(sizePolicy)
        self.textInnerMonitor.setMinimumSize(QtCore.QSize(75, 25))
        self.textInnerMonitor.setMaximumSize(QtCore.QSize(75, 25))
        self.textInnerMonitor.setFrame(False)
        self.textInnerMonitor.setReadOnly(True)
        self.textInnerMonitor.setObjectName("textInnerMonitor")
        self.horizontalLayout_10.addWidget(self.textInnerMonitor)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.textOuterMonitor = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOuterMonitor.sizePolicy().hasHeightForWidth())
        self.textOuterMonitor.setSizePolicy(sizePolicy)
        self.textOuterMonitor.setMinimumSize(QtCore.QSize(75, 25))
        self.textOuterMonitor.setMaximumSize(QtCore.QSize(75, 25))
        self.textOuterMonitor.setFrame(False)
        self.textOuterMonitor.setReadOnly(True)
        self.textOuterMonitor.setObjectName("textOuterMonitor")
        self.horizontalLayout_11.addWidget(self.textOuterMonitor)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.gridLayout.addWidget(self.groupBox, 0, 3, 8, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnActivateConnection = QtWidgets.QPushButton(self.centralwidget)
        self.btnActivateConnection.setObjectName("btnActivateConnection")
        self.horizontalLayout.addWidget(self.btnActivateConnection)
        self.textActivateConnectionNum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textActivateConnectionNum.sizePolicy().hasHeightForWidth())
        self.textActivateConnectionNum.setSizePolicy(sizePolicy)
        self.textActivateConnectionNum.setMaximumSize(QtCore.QSize(25, 25))
        self.textActivateConnectionNum.setAlignment(QtCore.Qt.AlignCenter)
        self.textActivateConnectionNum.setObjectName("textActivateConnectionNum")
        self.horizontalLayout.addWidget(self.textActivateConnectionNum)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.textCurrentConnection = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textCurrentConnection.sizePolicy().hasHeightForWidth())
        self.textCurrentConnection.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.textCurrentConnection.setFont(font)
        self.textCurrentConnection.setAutoFillBackground(False)
        self.textCurrentConnection.setAlignment(QtCore.Qt.AlignCenter)
        self.textCurrentConnection.setIndent(-1)
        self.textCurrentConnection.setObjectName("textCurrentConnection")
        self.gridLayout.addWidget(self.textCurrentConnection, 2, 0, 1, 2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnList = QtWidgets.QPushButton(self.centralwidget)
        self.btnList.setObjectName("btnList")
        self.horizontalLayout_8.addWidget(self.btnList)
        self.textListNum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textListNum.sizePolicy().hasHeightForWidth())
        self.textListNum.setSizePolicy(sizePolicy)
        self.textListNum.setMinimumSize(QtCore.QSize(25, 25))
        self.textListNum.setMaximumSize(QtCore.QSize(25, 25))
        self.textListNum.setFrame(False)
        self.textListNum.setAlignment(QtCore.Qt.AlignCenter)
        self.textListNum.setReadOnly(True)
        self.textListNum.setObjectName("textListNum")
        self.horizontalLayout_8.addWidget(self.textListNum)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout_2.addWidget(self.btnRun)
        self.textRunNum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textRunNum.sizePolicy().hasHeightForWidth())
        self.textRunNum.setSizePolicy(sizePolicy)
        self.textRunNum.setMaximumSize(QtCore.QSize(25, 25))
        self.textRunNum.setAlignment(QtCore.Qt.AlignCenter)
        self.textRunNum.setObjectName("textRunNum")
        self.horizontalLayout_2.addWidget(self.textRunNum)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_3.addWidget(self.btnStop)
        self.textStopNum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textStopNum.sizePolicy().hasHeightForWidth())
        self.textStopNum.setSizePolicy(sizePolicy)
        self.textStopNum.setMaximumSize(QtCore.QSize(25, 25))
        self.textStopNum.setAlignment(QtCore.Qt.AlignCenter)
        self.textStopNum.setObjectName("textStopNum")
        self.horizontalLayout_3.addWidget(self.textStopNum)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_4.addWidget(self.btnDelete)
        self.textDeleteNum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textDeleteNum.sizePolicy().hasHeightForWidth())
        self.textDeleteNum.setSizePolicy(sizePolicy)
        self.textDeleteNum.setMinimumSize(QtCore.QSize(25, 25))
        self.textDeleteNum.setMaximumSize(QtCore.QSize(25, 25))
        self.textDeleteNum.setAlignment(QtCore.Qt.AlignCenter)
        self.textDeleteNum.setObjectName("textDeleteNum")
        self.horizontalLayout_4.addWidget(self.textDeleteNum)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 2)
        self.btnDownLoad = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownLoad.setObjectName("btnDownLoad")
        self.gridLayout.addWidget(self.btnDownLoad, 7, 0, 1, 1)
        self.textDownloadUrl = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textDownloadUrl.sizePolicy().hasHeightForWidth())
        self.textDownloadUrl.setSizePolicy(sizePolicy)
        self.textDownloadUrl.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textDownloadUrl.setObjectName("textDownloadUrl")
        self.gridLayout.addWidget(self.textDownloadUrl, 7, 1, 1, 2)
        self.btnCurrentConnection.raise_()
        self.btnActivateConnection.raise_()
        self.textActivateConnectionNum.raise_()
        self.btnList.raise_()
        self.btnRun.raise_()
        self.textRunNum.raise_()
        self.btnStop.raise_()
        self.textStopNum.raise_()
        self.btnDelete.raise_()
        self.textDeleteNum.raise_()
        self.btnDownLoad.raise_()
        self.textDownloadUrl.raise_()
        self.textDownloadUrl.raise_()
        self.textBrowser.raise_()
        self.textCurrentConnectionNum.raise_()
        self.textListNum.raise_()
        self.groupBox.raise_()
        self.textCurrentConnection.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCmdHelp = QtWidgets.QAction(MainWindow)
        self.actionCmdHelp.setIcon(QtGui.QIcon(':about.ico'))
        self.actionCmdHelp.setObjectName("actionCmdHelp")
        self.actionCleanLog = QtWidgets.QAction(MainWindow)
        self.actionCleanLog.setIcon(QtGui.QIcon(':clean.ico'))
        self.actionCleanLog.setObjectName("actionCleanLog")
        self.actionSoftInfo = QtWidgets.QAction(MainWindow)
        self.actionSoftInfo.setIcon(QtGui.QIcon(':about.ico'))
        self.actionSoftInfo.setObjectName("actionSoftInfo")
        self.actionVisitUs = QtWidgets.QAction(MainWindow)
        self.actionVisitUs.setIcon(QtGui.QIcon(':visit.ico'))
        self.actionVisitUs.setObjectName("actionVisitUs")
        self.actionImportCfg = QtWidgets.QAction(MainWindow)
        self.actionImportCfg.setIcon(QtGui.QIcon(':file.ico'))
        self.actionImportCfg.setObjectName("actionImportCfg")
        self.menu.addAction(self.actionImportCfg)
        self.menu_2.addAction(self.actionCmdHelp)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionCleanLog)
        self.menu_3.addAction(self.actionSoftInfo)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionVisitUs)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dthing远程桌面"))
        self.btnCurrentConnection.setText(_translate("MainWindow", "当前连接"))
        self.textCurrentConnectionNum.setText(_translate("MainWindow", "0"))
        self.groupBox.setTitle(_translate("MainWindow", "状态管理"))
        self.label.setText(_translate("MainWindow", "CPU电压监测："))
        self.label_6.setText(_translate("MainWindow", "CPU温度检测："))
        self.label_2.setText(_translate("MainWindow", "内存状态统计："))
        self.label_3.setText(_translate("MainWindow", "外部存储容量："))
        self.label_4.setText(_translate("MainWindow", "内部存储监控："))
        self.label_5.setText(_translate("MainWindow", "外部存储监控："))
        self.btnActivateConnection.setText(_translate("MainWindow", "激活连接"))
        self.textCurrentConnection.setText(_translate("MainWindow", "当前没有连接被激活"))
        self.btnList.setText(_translate("MainWindow", "应用列表"))
        self.textListNum.setText(_translate("MainWindow", "0"))
        self.btnRun.setText(_translate("MainWindow", "运行应用"))
        self.btnStop.setText(_translate("MainWindow", "停止应用"))
        self.btnDelete.setText(_translate("MainWindow", "删除应用"))
        self.btnDownLoad.setText(_translate("MainWindow", "远程下载"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.actionCmdHelp.setText(_translate("MainWindow", "查看命令"))
        self.actionCleanLog.setText(_translate("MainWindow", "清除日志"))
        self.actionSoftInfo.setText(_translate("MainWindow", "软件信息"))
        self.actionVisitUs.setText(_translate("MainWindow", "访问我们"))
        self.actionImportCfg.setText(_translate("MainWindow", "导入配置"))

