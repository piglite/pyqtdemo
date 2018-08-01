import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PaintEvent Demo')
        self.idx = 1
        self.mypics = {1:'image/left.png',2:'image/up.png',3:'image/right.png',4:'image/down.png'}
        self.mypix()
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()


    def mypix(self):
        self.update()
        if self.idx == 5:
            self.idx = 1
        self.pix = QPixmap(self.mypics.get(self.idx))
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, event):
        p = QPainter(self)
        p.drawPixmap(self.rect(),self.pix)

    def timeChange(self):
        self.idx += 1
        self.mypix()

    def mouseDoubleClickEvent(self, event):
        print('全局坐标：',event.globalPos())
        print('当前坐标：',event.pos())



app = QApplication(sys.argv)
m = MyWin()
m.show()#
sys.exit(app.exec())



















