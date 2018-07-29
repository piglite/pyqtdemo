import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn1 = QPushButton('按钮1')
        self.btn2 = QPushButton('按钮2')
        self.btn2.setProperty('name','my')
        layout = QVBoxLayout(self)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.resize(640,480)
        self.setWindowTitle('QSS Demo')

app = QApplication(sys.argv)
w = MyWindow()
w.setObjectName('MyWin')
qss = '''
    QPushButton[name='my']{color:red;}
    #MyWin{background-color:blue;}
'''
w.setStyleSheet("#MyWin{border-image:url(image/python.jpg);}")
w.show()
sys.exit(app.exec())