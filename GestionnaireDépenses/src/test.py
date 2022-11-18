import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                               QDateTimeEdit, QDial, QDoubleSpinBox,
                               QFontComboBox, QGridLayout, QLabel, QLCDNumber,
                               QLineEdit, QMainWindow, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox,
                               QTabWidget, QTimeEdit, QVBoxLayout, QWidget, QFormLayout,
                               QHBoxLayout, QTableWidget, QTableWidgetItem)

from Budget import Budget
from Data import Data

def printTable():
    # loading of the files countained in the repertory
    choixMois = QComboBox()
    data = Data()
    data.loadFile()
    listMois = data.getMois()
    for i in range(len(listMois)):
        choixMois.addItem(listMois[i])

    # creation of a list of categories with the different budgets
    categories = []
    b = Budget()
    b.addBudget("Nourriture", 120, 0)
    b.addBudget("Déplacement", 150, 0)
    for i in range(len(b.budgets)):
        elem:Budget = b.budgets[i]
        categories.append(elem.getNom())
    
    path = '../assets/files/' + choixMois.currentText() # construction of the path where the file to be read is to be fetched
    data.tidyData(path) # storing data in a list
    tableWidget = QTableWidget(len(data.getDepenses()), 5, self) # creation of the table
    tableWidget.setHorizontalHeaderLabels(['Date', 'Libellé', 'Sortie', 'Entrée', 'Catégorie']) # addition of columns

    # loop for displaying data in the table
    for i in range(tableWidget.rowCount()):
        date = QTableWidgetItem(data.getDate(i))
        tableWidget.setItem(i, 0, date)
        libelle = QTableWidgetItem(data.getLibelle(i))
        tableWidget.setItem(i, 1, libelle)
        sortie = QTableWidgetItem(str(data.getSortie(i)))
        tableWidget.setItem(i, 3, sortie)
        entree = QTableWidgetItem(str(data.getEntree(i)))
        tableWidget.setItem(i, 2, entree)
        choixCat = QComboBox()
        for j in range(len(categories)):
            choixCat.addItem(categories[j])            
            tableWidget.setCellWidget(i, 4, choixCat)