import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PaintEvent Demo')
        self.resize(640,480)
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap('image/python.jpg')
        #painter.setBrush(Qt.black)
        painter.drawPixmap(self.rect(),pixmap)

app = QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec())
