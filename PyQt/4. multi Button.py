import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonUI()
        self.initUI()

    def buttonUI(self):
        btn1 = QPushButton('Button',self)
        btn1.setToolTip('This is a Button')
        btn1.resize(btn1.sizeHint())
        btn1.move(100,100)

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Hello World')
        self.show()

app = QApplication(sys.argv)
exe = HelloWorld()
# app.setWindowIcon(QIcon('Hello-World.png'))

sys.exit(app.exec_())