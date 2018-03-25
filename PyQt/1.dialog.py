import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)

app = QApplication([])  # 어플리케이션 생성

dialog = QInputDialog()  # 다이얼로그 생성
dialog.show()            # 다이얼로그 띄우기

app.exec_()              #
