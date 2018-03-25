


import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  # application 객체 생성

w = QWidget()  # default Interface 선언
w.setWindowTitle('Hello World')  # 제목 설정
w.show()  # 스크린에 띄우기

sys.exit(app.exec_())  # app을 끄는 버튼을 누르기 전까진 loop를 돌고 있다.
