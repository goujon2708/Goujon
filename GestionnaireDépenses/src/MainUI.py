import sys, os
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
          self.dicoBudgets = []
          
          
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

          # setup des Widgets
          layout.addWidget(choixMois)
          layout.addWidget(self.printDepenseTab())
          
          # affichage du layout principal
          self.tabDepense.setLayout(layout)


     
     
     
     """print the table of depense in the layout
     """
     def printDepenseTab(self):
          
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
               for j in range(len(self.budgets.budgets)):
                    
                    choixCat.addItem(str(self.budgets.getNomTab(j)))
                    tableWidget.setCellWidget(i, 4, choixCat)

          return tableWidget
          
     
     
     def budgetsTab(self):

          # creation of the different layouts
          layout = QVBoxLayout()

          # loading of the files countained in the repertory
          choixMois = QComboBox()
          # récupération des mois
          # pas d'appel à loadFile() car sinon création de doublons
          listMois = self.data.getMois()

          # ajout des mois dans la ComboBox de choix des mois 
          for i in range(len(listMois)):
               
               choixMois.addItem(listMois[i])

          # création du tableau représentant la situation des dépenses par rapport au budget
          situationBudgetsTab = QTableWidget(len(self.budgets.budgets), 2, self)
          # setup des colonnes 
          situationBudgetsTab.setHorizontalHeaderLabels(['Nom Budget', 'Situation Budget'])
          
          # rangement des valeurs dans le tableau
          for j in range(situationBudgetsTab.rowCount()):
               
               nom = QTableWidgetItem(self.budgets.getNomTab(j))
               # rangement de la valeur à la position courante
               situationBudgetsTab.setItem(j, 0, nom)
               # on veut savoir à combien nous sommes de la limite de budget fixée
               situation = QTableWidgetItem("0" + "/" + str(self.budgets.getMontantMaxTab(j)))
               # rangement de la valeur à la position courante
               situationBudgetsTab.setItem(j, 1, situation)
          
          
          dateLabel = QLabel("Nom")
          lineEdit1 = QLineEdit()        
          montantLabel = QLabel("MontantMax")
          lineEdit2 = QLineEdit()
          
          addButton = QPushButton("Ajouter", self)  
          addButton.setCheckable(True)
          
          addButton.clicked.connect(lambda: self.majBudget(lineEdit1.text(), lineEdit2.text()))

          # ajout des Widget dans le layout principal
          layout.addWidget(choixMois)
          layout.addWidget(self.printBudgetsTab())
          layout.addWidget(situationBudgetsTab)
          layout.addWidget(dateLabel)
          layout.addWidget(lineEdit1)
          layout.addWidget(montantLabel)
          layout.addWidget(lineEdit2)
          layout.addWidget(addButton)

          # affichage de ce layout
          self.tabBudgets.setLayout(layout)

     
     
     def majBudget(self, nomBudget: QLineEdit, montantMax: QLineEdit):
          # ajout du budget dans le fichier Budget.txt
          self.budgets.addBudgetInFile(nomBudget, montantMax)
          # mise à jour de l'affichage
          self.printBudgetsTab()
     
     
     
     def printBudgetsTab(self):
          
          # creation of the table
          budgetsTab = QTableWidget(len(self.budgets.budgets), 2, self)
          # addition of columns
          budgetsTab.setHorizontalHeaderLabels(['Nom Budget', 'Montant Budget']) 
          
          budgetsTab.clearContents()

          self.remplirDico()

          # rangement des valeurs dans le tableau des budgets
          for i in range(budgetsTab.rowCount()):

               nom = QTableWidgetItem(self.dicoBudgets.index)
               budgetsTab.setItem(i, 0, nom)
               
               montantMax = QTableWidgetItem(str(self.budgets.getMontantMaxTab(i)))
               budgetsTab.setItem(i, 1, montantMax)

          return budgetsTab
     
     
     
     
     
     def remplirDico(self):
          f = open("Budgets.txt", "r")
          ligne = None
          if(os.path.getsize("Budgets.txt") != 0):
               ligne = f.readline()
               budgetCour = ligne.split(' ')
               self.dicoBudgets.append(budgetCour)
               i = 1
          i = 0
          while(ligne != ''):
               ligne = f.readline()
               budgetCour = ligne.split(' ')
               self.dicoBudgets.append(budgetCour)
               i = i + 1
          f.close()
          print(self.dicoBudgets)

     
     
     def addToDico(self, key, value):
          self.dicoBudgets[key] = value


     
     
     
     
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