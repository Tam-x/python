from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QLabel
from Config.Config import Config

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.resize(350, 180)
        self.setWindowTitle('关于')
        self.setWindowIcon((QtGui.QIcon(':about.ico')))
        label=QLabel('版本：'+ Config.VERSION, self)
        label.move(25, 30)
        label=QLabel('名称：DTU数据生产模拟器', self)
        label.move(25, 60)
        label=QLabel('运行环境：windows8 64位环境下编译', self)
        label.move(25, 90)
        label=QLabel('版权@2017-2018成都雅鲁科技所有', self)
        label.move(25, 120)