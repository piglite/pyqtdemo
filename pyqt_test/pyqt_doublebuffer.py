import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Double Buffer')
        self.pix = QPixmap(400,400)
        self.pix.fill(Qt.white)
        self.startPoint = QPoint()
        self.endPoint = QPoint()
        self.temp = QPixmap()

        self.isDrawing = False
        self.resize(500,500)

    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.startPoint.x()
        y = self.startPoint.y()
        w = self.endPoint.x()-x
        h = self.endPoint.y()-y
        if self.isDrawing:
            self.temp = QPixmap(self.pix)
            p1 = QPainter(self.temp)
            p1.drawRect(x,y,w,h)
            painter.drawPixmap(0,0,self.temp)
        else:
            p2 = QPainter(self.pix)
            p2.drawRect(x,y,w,h)
            painter.drawPixmap(0,0,self.pix)

    def mouseMoveEvent(self, event):
        if event.buttons()==Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()
            self.isDrawing = True
    def mousePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True
    def mouseReleaseEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.isDrawing = False
            self.update()

app = QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec())