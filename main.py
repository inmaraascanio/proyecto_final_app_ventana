from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from instructions import *
from test import TestWindow


class MainWindow(QWidget):
    def __init__(self, title= 'Ruffier Test'):
        super().__init__()
        self.setObjectName("MainWindow")
        self.title = title

        self.set_ui()
        self.config_win()
        self.connections()
        self.show()

    def set_ui(self):
        # Elementos gráficos
        self.hello_text = QLabel('¡Bienvenido al Programa de detección de estado de salud!')
        self.instruction = QLabel(
            'Esta aplicación le permite usar la prueba de Ruffier para realizar un diagnóstico inicial de su salud.\n'
            'La prueba de Ruffier es un conjunto de ejercicios físicos diseñado para evaluar su rendimiento cardíaco.\n'
            'El sujeto se tumba en posición supina durante 5 minutos y se toma la frecuencia del pulso durante 15 segundos;\n'
            'Luego, dentro de 45 segundos, el sujeto realiza 30 sentadillas.\n'
            'Cuando el ejercicio termina, se toman sus pulsaciones de nuevo durante 15 segundos\n'
            'y luego durante los últimos 15 segundos del primer minuto de recuperación.\n'
            '¡Importante! Si no se siente bien durante la prueba, deténgala y consulte con un médico.')
        
        self.btn_next = QPushButton('Iniciar', self)
        # Layout principal
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.layout_line)

    def config_win(self):
        self.setWindowTitle(self.title)
        self.resize(1000, 600)
        self.move(200, 100)
       
    def connections(self):
        self.btn_next.clicked.connect(self.next_click)
        pass

    def next_click(self):
        self.test_window = TestWindow()
        self.hide()
        pass


if __name__ == '__main__':
    app = QApplication([])
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    mw = MainWindow()
    mw.show()
    app.exec()
