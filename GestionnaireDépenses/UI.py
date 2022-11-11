import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QComboBox, QWidget


class UI(QMainWindow):

    # def set_style(self):
    #     with open('./style', 'r') as f:
    #         self.setStyleSheet(f.read())

    def __init__(self):
        super().__init__()
        # self.set_style()

        self.setWindowTitle("Gestionnaire de dépenses")
        self.setFixedSize(QSize(1500, 950))

        layout = QVBoxLayout()

        comboBox = QComboBox()
        comboBox.addItems(['Octobre'])

        button = QPushButton('Click Me')
        button.setCheckable(True)
        button.clicked.connect(self.functionEvent)

        self.setCentralWidget(button)


        layout.addWidget(comboBox)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



        
    def functionEvent(self):
        print("Clicked !!")
        

app = QApplication(sys.argv)

window = UI()
window.show()

app.exec_()
