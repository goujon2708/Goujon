import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QTabWidget, QTableWidgetItem, QMainWindow, QFormLayout, QLineEdit, QVBoxLayout, QComboBox, QWidget, QTableWidget
from Bilan import Bilan
from Budget import Budget
from Data import Data

class DepenseUI(QMainWindow):

    # def set_style(self):
    #     with open('./style', 'r') as f:
    #         self.setStyleSheet(f.read())

    def __init__(self):
        super().__init__()
        # # self.set_style()

        

        # creation of the different layouts
        layout = QVBoxLayout()

        # loading of the files countained in the repertory
        choixMois = QComboBox()
        data = Data()
        data.loadFile()
        listMois = data.getMois()
        for i in range(len(listMois)):
            choixMois.addItem(listMois[i])

        layout.addWidget(choixMois)

        tab = QWidget()
        tab.setLayout(layout)
        self.setCentralWidget(tab)

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
        
        layout.addWidget(tableWidget)
        layout.addWidget(choixCat)