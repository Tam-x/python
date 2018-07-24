from PyQt5.QtWidgets import QMainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

    def set_close(self, a):
        self.close = a

    def closeEvent(self, event):
        try:
            self.close()
        except:
            pass
        super(MyMainWindow, self).closeEvent(event)