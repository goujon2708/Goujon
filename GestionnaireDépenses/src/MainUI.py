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
          self.clearDico()
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
               nom = QTableWidgetItem(self.dicoBudgets[i][0])
               budgetsTab.setItem(i, 0, nom)
               
               montantMax = QTableWidgetItem(self.dicoBudgets[i][1])
               budgetsTab.setItem(i, 1, montantMax)

          return budgetsTab
     
     
     
     
     """Lis les budgets présents dans le fichier et les range dans le dictionnaire
     """
     def remplirDico(self):
          # ouverture du budget en lecture
          f = open("Budgets.txt", "r")
          ligne = None
          # nettoyage du dico pour éviter les doublons
          self.dicoBudgets.clear()
         
         # parcours du fichier
          while(ligne != ''):
               
               # lecture de la ligne courante
               ligne = f.readline()
               # récupération des 2 champs de la ligne courante dans une liste
               budgetCour = ligne.split(' ')
               # ajout de cette liste dans le dico
               self.dicoBudgets.append(budgetCour)
               
          f.close()
          self.clearDico()


     """supprime les listes vides créées par le dictionnaire
     """
     def clearDico(self):
          # parcours du dictionnaire
          for i in range(len(self.dicoBudgets)):
               
               # si la liste courante est vide, alors elle est supprimée du dico
               if(self.dicoBudgets[i][0] == ''):
                    self.dicoBudgets.pop(i)
          

     
     
     
     
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