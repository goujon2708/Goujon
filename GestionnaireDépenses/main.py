from PyQt5.QtWidgets import QApplication, QWidget

import sys
from ClassementDonnees import ClassementDonnees

# app = QApplication(sys.argv)
# window = QWidget()
# window.show() 
# app.exec()

print(ClassementDonnees.calculExpenses("assets/files/octobre.csv", 'Débit euros'))