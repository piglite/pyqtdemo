import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PaintEvent Demo')
        self.pix = QPixmap('image/mask.png')
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap('image/desktop.jpg')
        #painter.setBrush(Qt.black)
        painter.drawPixmap(self.rect(),pixmap)

app = QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec())
