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
          # onglet "Dépenses"
          self.tabDepense = QWidget()
          # onglet "Budgets"
          self.tabBudgets = QWidget()
          # onglet "Bilan"
          self.tabBilan = QWidget()


          self.data = Data()
          self.budgets = Budget()
          
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

          # loading of the files countained in the repertory
          choixMois = QComboBox()
          # chargement du fichier correspond à la valeur courant de la ComboBox
          self.data.loadFile()
          # récupération des mois
          listMois = self.data.getMois()

          # ajout des mois dans la ComboBox de choix des mois 
          for i in range(len(listMois)):
               
               choixMois.addItem(listMois[i])
          
          # construction of the path where the file to be read is to be fetched
          path = '../assets/files/' + choixMois.currentText()
          # storing data in a list
          self.data.tidyData(path)  

          # creation of a list of categories with the different budgets
          categories = []
          b = Budget()
          b.addBudget("Nourriture", 120, 0)
          b.addBudget("Déplacement", 150, 0)

          # ajout des budgets dans la ComboBox relative aux budgets (colonne "catégorie" dans le tableau)
          for i in range(len(b.budgets)):
               
               elem: Budget = b.budgets[i]
               categories.append(elem.getNom())

          # setup des Widgets
          layout.addWidget(choixMois)
          layout.addWidget(self.printTable())
          
          # affichage du layout principal
          self.tabDepense.setLayout(layout)


     
     
     
     """print the table in the layout
     """
     def printTable(self):
          # creation of the different layouts
          layout = QVBoxLayout()

          # creation of a list of categories with the different budgets
          categories = []
          b = Budget()
          b.addBudget("Nourriture", 120, 0)
          b.addBudget("Déplacement", 150, 0)

          
          # creation of the table
          tableWidget = QTableWidget(len(self.data.getDepenses()), 5, self)  
          # addition of columns
          tableWidget.setHorizontalHeaderLabels(['Date', 'Libellé', 'Sortie', 'Entrée', 'Catégorie'])  

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
               # ajout de comboBox à chaque ligne de la colonne "catégorie"
               for j in range(len(categories)):
                    
                    choixCat.addItem(categories[j])
                    tableWidget.setCellWidget(i, 4, choixCat)

          return tableWidget

     
     
     
     def budgetsTab(self):
          # creation of the different layouts
          layout = QVBoxLayout()

          # loading of the files countained in the repertory
          choixMois = QComboBox()
          self.data.loadFile()
          listMois = self.data.getMois()

          # ajout des mois dans une liste de mois
          for i in range(len(listMois)):
               
               choixMois.addItem(listMois[i])

          # ajout des budgets principaux
          self.budgets.addBudget("Nourriture", 120, 0)
          self.budgets.addBudget("Déplacement", 150, 0)
          self.budgets.addBudget("Abonnement", 13, 0)
          self.budgets.addBudget("Gloubiboulga", 20, 0)
          self.budgets.addBudget("Soirées", 30, 0)
          self.budgets.addBudget("Assurance", 53, 0)
          self.budgets.addBudget("Loyer", 325, 0)
          self.budgets.addBudget("Charges", 25, 0)
          self.budgets.addBudget("Divers", 70, 0)
          
          # creation of the table
          tableWidget = QTableWidget(len(self.budgets.budgets), 2, self)
          # addition of columns
          tableWidget.setHorizontalHeaderLabels(['Nom Budget', 'Montant Budget']) 

          # rangement des valeurs dans le tableau des budgets
          for i in range(tableWidget.rowCount()):

               nom = QTableWidgetItem(self.budgets.getNomTab(i))
               tableWidget.setItem(i, 0, nom)
               
               situation = QTableWidgetItem(str(self.budgets.getMontantMaxTab(i)))
               tableWidget.setItem(i, 1, situation)

          # ajout des Widget dans le layout principal
          layout.addWidget(choixMois)
          layout.addWidget(tableWidget)

          # affichage de ce layout
          self.tabBudgets.setLayout(layout)

     
     
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