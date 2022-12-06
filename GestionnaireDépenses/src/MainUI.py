import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                               QDateTimeEdit, QDial, QDoubleSpinBox, QFontComboBox,
                               QGridLayout, QLabel, QLCDNumber, QLineEdit, QMainWindow,
                               QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox,
                               QTabWidget, QTimeEdit, QVBoxLayout, QWidget, QFormLayout,
                               QHBoxLayout, QTableWidget, QTableWidgetItem)
from Budget import Budget
from Data import Data


class MainUI(QTabWidget):

     def __init__(self, parent=None):

          super(MainUI, self).__init__(parent)
          self.tabDepense = QWidget()
          self.tabBudgets = QWidget()
          self.tabBilan = QWidget()

          self.data = Data()
          self.addTab(self.tabDepense, "Dépenses")
          self.addTab(self.tabBudgets, "Budgets")
          self.addTab(self.tabBilan, "Bilan")
          self.depenseTab()
          self.budgetsTab()
          self.bilanTab()
          self.setWindowTitle("Gestionnaire de dépense")
          self.setFixedSize(QSize(1350, 750))

     
     
     def depenseTab(self):

          layout = QVBoxLayout()
          # addition's form
          dateLabel = QLabel("Date")
          lineEdit1 = QDateEdit()
          libelleLabel = QLabel("Libelle")
          lineEdit2 = QLineEdit()
          sortieLabel = QLabel("Sortie")
          lineEdit3 = QLineEdit()
          entreeLabel = QLabel("Entrée")
          lineEdit4 = QLineEdit()
          catLabel = QLabel("Catégorie")
          lineEdit5 = QComboBox()

          # creation of a list of categories with the different budgets
          categories = []
          b = Budget()
          b.addBudget("Nourriture", 120, 0)
          b.addBudget("Déplacement", 150, 0)

          for i in range(len(b.budgets)):
               elem: Budget = b.budgets[i]
               categories.append(elem.getNom())
               for j in range(len(categories)):
                    lineEdit5.addItem(categories[j])
               
          addButton = QPushButton("Ajouter", self)
          addButton.setCheckable(True)
          addButton.clicked.connect(lambda: self.majDepense(lineEdit1.text(),
                                                  lineEdit2.text(),
                                                  lineEdit3.text(),
                                                  lineEdit4.text()
                                                  ))

          layout.addWidget(self.printTable())
          layout.addWidget(dateLabel)
          layout.addWidget(lineEdit1)
          layout.addWidget(libelleLabel)
          layout.addWidget(lineEdit2)
          layout.addWidget(sortieLabel)
          layout.addWidget(lineEdit3)
          layout.addWidget(entreeLabel)
          layout.addWidget(lineEdit4)
          layout.addWidget(catLabel)
          layout.addWidget(lineEdit5)
          layout.addWidget(addButton)
          
          self.tabDepense.setLayout(layout)

     
     
     
     """when the "add" button is clicked, triggers this event which adds the new expense to the list
     """
     def majDepense(self, date: QDateEdit, libelle: QLineEdit, sortie: QLineEdit, entree: QLineEdit):
          self.data.addDepense(date, libelle, sortie, entree)
          self.data.printList()
          self.printTable()

     
     
     
     """print the table in the layout
     """
     def printTable(self):
          # creation of the different layouts
          layout = QVBoxLayout()

          # loading of the files countained in the repertory
          choixMois = QComboBox()
          self.data.loadFile()
          listMois = self.data.getMois()

          for i in range(len(listMois)):
               choixMois.addItem(listMois[i])

          # creation of a list of categories with the different budgets
          categories = []
          b = Budget()
          b.addBudget("Nourriture", 120, 0)
          b.addBudget("Déplacement", 150, 0)

          for i in range(len(b.budgets)):
               elem: Budget = b.budgets[i]
               categories.append(elem.getNom())

          # construction of the path where the file to be read is to be fetched
          path = '../assets/files/' + choixMois.currentText()
          self.data.tidyData(path)  # storing data in a list
          print("Taille de la liste : ", len(self.data.depenses))
          tableWidget = QTableWidget(len(self.data.getDepenses()), 5, self)  # creation of the table
          tableWidget.setHorizontalHeaderLabels(['Date', 'Libellé', 'Sortie', 'Entrée', 'Catégorie'])  # addition of columns

          # loop for displaying data in the table
          for i in range(tableWidget.rowCount()):
               date = QTableWidgetItem(self.data.getDate(i))
               tableWidget.setItem(i, 0, date)
               libelle = QTableWidgetItem(self.data.getLibelle(i))
               tableWidget.setItem(i, 1, libelle)
               sortie = QTableWidgetItem(str(self.data.getSortie(i)))
               tableWidget.setItem(i, 3, sortie)
               entree = QTableWidgetItem(str(self.data.getEntree(i)))
               tableWidget.setItem(i, 2, entree)
               choixCat = QComboBox()
               for j in range(len(categories)):
                    choixCat.addItem(categories[j])
                    tableWidget.setCellWidget(i, 4, choixCat)

          return tableWidget

     
     
     
     def budgetsTab(self):
          # layout = QVBoxLayout()
          # layout.addWidget(self.printTable())
          # self.tabBudgets.setLayout(layout)
          return

     
     
     def bilanTab(self):

          layout = QHBoxLayout()
          layout.addWidget(QLabel("subjects"))
          layout.addWidget(QCheckBox("Physics"))
          layout.addWidget(QCheckBox("Maths"))
          self.setTabText(2, "Bilan")
          self.tabBilan.setLayout(layout)


     def main():
          
          app = QApplication(sys.argv)
          ex = MainUI()
          ex.show()
          sys.exit(app.exec())


     if __name__ == '__main__':
          main()