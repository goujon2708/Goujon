# import pandas as pd

# data = pd.read_csv("octobre.csv", sep=';')
# print(data)

from PyQt5.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)
window = QWidget()
window.show() 
app.exec()
