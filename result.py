from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from instructions import TXT_RESULT_TITLE, TXT_INDEX, TXT_WORKOUT


class ResultWindow(QWidget):
    def __init__(self, exp=None, title=TXT_RESULT_TITLE):
        super().__init__()
        self.setObjectName("ResultWindow")
        self.title = title
        self.exp = exp  # Recibe la información del usuario/evaluación si es necesario

        self.set_ui()
        self.config_win()
        self.connections()
        self.show()

    def set_ui(self):
        self.index_label = QLabel(TXT_INDEX)
        self.result_label = QLabel(TXT_WORKOUT)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_label, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.result_label, alignment=Qt.AlignCenter)
        
        self.setLayout(self.layout_line)

    def results(self):
        if self.exp is None:
            return "0"
        
        # Ejemplo tomando los pulsos desde self.exp
        p1 = int(self.exp.p1)
        p2 = int(self.exp.p2)
        p3 = int(self.exp.p3)
        
        index = (p1 + p2 + p3 - 200) / 10
        return str(index)


    def config_win(self):
        self.setWindowTitle(self.title)
        self.resize(1000, 600)
        self.move(200, 100)

    def connections(self):
        pass



if __name__ == '__main__':
    app = QApplication([])
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    mw = ResultWindow()
    mw.show()
    app.exec()
