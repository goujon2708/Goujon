import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                               QDateTimeEdit, QDial, QDoubleSpinBox,
                               QFontComboBox, QGridLayout, QLabel, QLCDNumber,
                               QLineEdit, QMainWindow, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox,
                               QTabWidget, QTimeEdit, QVBoxLayout, QWidget, QFormLayout,
                               QHBoxLayout, QTableWidget, QTableWidgetItem)

from DepenseUI import DepenseUI
from Budget import Budget
from Data import Data

# class Main(QTabWidget):
#      def __init__(self, parent = None) -> None:
#           super(Main, self).__init__(parent)
#           self.depenseTab = QWidget()
#           self.budgetTab = QWidget()
#           self.bilanTab = QWidget()
          
#           self.addTab(self.depenseTab, "Dépenses")
#           self.addTab(self.budgetTab, "Budgets")
#           self.addTab(self.bilanTab, "Bilan")
          
#           d = DepenseUI()
#           budg = BudgetsUI()
#           bilan = BilanUI()
#           self.setWindowTitle("Gestionnaire de dépenses")
#           self.setFixedSize(QSize(1300, 750))
          
# app = QApplication(sys.argv)

# window = Main()
# window.show()

# app.exec()

class tabdemo(QTabWidget):
     def __init__(self, parent = None):
          super(tabdemo, self).__init__(parent)
          self.tabDepense = QWidget()
          self.tabBudgets = QWidget()
          self.tabBilan = QWidget()

          self.addTab(self.tabDepense,"Dépenses")
          self.addTab(self.tabBudgets,"Budgets")
          self.addTab(self.tabBilan,"Bilan")
          self.depenseTab()
          self.budgetsTab()
          self.bilanTab()
          self.setWindowTitle("Gestionnaire de dépense")
          self.setFixedSize(QSize(1350,750))
		
     def depenseTab(self):
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
          
          self.tabDepense.setLayout(layout)
		
     
     
     def budgetsTab(self):
          layout = QFormLayout()
          sex = QHBoxLayout()
          sex.addWidget(QRadioButton("Male"))
          sex.addWidget(QRadioButton("Female"))
          layout.addRow(QLabel("Sex"),sex)
          layout.addRow("Date of Birth",QLineEdit())
          self.setTabText(1,"Budgets")
          self.tabBudgets.setLayout(layout)
		
     
     
     def bilanTab(self):
          layout = QHBoxLayout()
          layout.addWidget(QLabel("subjects")) 
          layout.addWidget(QCheckBox("Physics"))
          layout.addWidget(QCheckBox("Maths"))
          self.setTabText(2,"Bilan")
          self.tabBilan.setLayout(layout)
		


def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec())
	
if __name__ == '__main__':
   main()