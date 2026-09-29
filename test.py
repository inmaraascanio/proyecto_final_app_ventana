from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLineEdit, QApplication
)
from instructions import *
from result import ResultWindow
from PyQt5.QtGui import QFont


class TestWindow(QWidget):
    def __init__(self, title=TXT_TEST_TITLE):
        super().__init__()
        self.setObjectName("TestWindow")
        self.title = title
        self.set_ui()
        self.config_win()
        self.connections()
        self.show()

    def set_ui(self):
        # Textos (Labels)
        self.name = QLabel(TXT_NAME)
        self.age = QLabel(TXT_AGE)
        self.test_1 = QLabel(TXT_TEST1)
        self.test_2 = QLabel(TXT_TEST2)
        self.test_3 = QLabel(TXT_TEST3)
        self.timer_label = QLabel ('00:00:15')
        self.timer_label.setObjectName("timer_label")

        # Inputs
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText(TXT_NAME_INPUT)
        self.age_input = QLineEdit()
        self.pulse1_input = QLineEdit()
        self.pulse2_input = QLineEdit()
        self.pulse3_input = QLineEdit()
        #Botones
        self.btn_test1 = QPushButton(TXT_START_TEST1)
        self.btn_test2 = QPushButton(TXT_START_TEST2)
        self.btn_test3 = QPushButton(TXT_START_TEST3)
        self.btn_result = QPushButton(TXT_SEND_RESULTS)

        #LAYOUT
        self.main_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
        #Insertar elementos
        #Columna 1
        self.col1.addWidget(self.name, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.name_input, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.age, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.age_input, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.test_1, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.test_2, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.test_3, alignment=Qt.AlignLeft)
        self.col1.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        

        #Columna 2
        self.col2.addWidget(self.timer_label, alignment=Qt.AlignRight)

        #Implementación del layout
        self.main_layout.addLayout(self.col1)
        self.main_layout.addLayout(self.col2)
        self.setLayout(self.main_layout)



    def config_win(self):
        self.setWindowTitle(self.title)
        self.resize(1000, 600)
        self.move(200, 100)

    def connections(self):
        self.btn_result.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.run_timer1)
        self.btn_test2.clicked.connect(self.run_timer2)
        self.btn_test1.clicked.connect(self.run_timer3)

    def run_timer1(self):
        self.count = QTime (0, 0, 15)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer1)
        self.timer.start(1000)

    def update_timer1(self):
        self.count = self.count.addSecs(-1)
        self.timer_label.setText(self.count.toString("hh:mm:ss"))
        if self.count.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def run_timer2(self):
            self.count = QTime (0, 0, 45)
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_timer2)
            self.timer.start(1000)
    
    def update_timer2(self):
        self.count = self.count.addSecs(-1)
        self.timer_label.setText(self.count.toString("hh:mm:ss"))
        if self.count.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def run_timer3(self):
                self.count = QTime (0, 1, 0)
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.update_timer3)
                self.timer.start(1000)
        
    def update_timer3(self):
        self.count = self.count.addSecs(-1)
        self.timer_label.setText(self.count.toString("hh:mm:ss"))
        if self.count.toString("hh:mm:ss") == "00:00:00":
             self.timer.stop()

    
    def next_click(self):
        self.hide()
        self.exp = ResultWindow()
        

if __name__ == '__main__':
    app = QApplication([])
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    mw = TestWindow()
    mw.show()
    app.exec()
        
        
  
