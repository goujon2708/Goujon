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
          self.budgetsTab = QTableWidget()
          self.situationBudgetsTab = QTableWidget()

          # replisssage du dico avec les valeurs présentes dans le fichier
          self.remplirDico()

          # création d'un tableau vide
          self.budgetsTab = QTableWidget(len(self.dicoBudgets), 2, self)
          # addition of columns
          self.budgetsTab.setHorizontalHeaderLabels(['Nom Budget', 'Montant Budget']) 

          # création d'un tableau vide
          self.situationBudgetsTab = QTableWidget(len(self.dicoBudgets), 2, self)
          self.situationBudgetsTab.setHorizontalHeaderLabels(['Nom Budget', 'Situation Budget'])
          
          
          self.addTab(self.tabDepense, "Dépenses")
          self.addTab(self.tabBudgets, "Budgets")
          self.addTab(self.tabBilan, "Bilan")
          
          # affichage des onglets
          self.ongletDepense()
          self.ongletBudgets()
          self.bilanTab()
          
          # paramètres de la fenêtre
          self.setWindowTitle("Gestionnaire de dépense")
          self.setFixedSize(QSize(1350, 750))

     
     
     
     
     def ongletDepense(self):

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
          
     
     
     def ongletBudgets(self):

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

          # remplissage du dictionnaire avec les valeurs présentes dans le fichier
          self.remplirDico()
               
          # rangement des valeurs dans le tableau des situations
          for j in range(len(self.dicoBudgets)-1):
               
               nom = QTableWidgetItem(self.dicoBudgets[j][0])
               # rangement de la valeur à la position courante
               self.situationBudgetsTab.setItem(j, 0, nom)

               s = str(self.dicoBudgets[j][1])

               # on veut savoir à combien nous sommes de la limite de budget fixée
               situation = QTableWidgetItem("0" + "/" + s[:-1].strip())
               # rangement de la valeur à la position courante
               self.situationBudgetsTab.setItem(j, 1, situation)
               
          j = len(self.dicoBudgets)-1
          
          # ajout du dernier élément en dur pas de '\n' ) supprimer
          nom = QTableWidgetItem(self.dicoBudgets[j][0])
          self.situationBudgetsTab.setItem(j, 0, nom)

          s = str(self.dicoBudgets[j][1])
          situation = QTableWidgetItem("0" + "/" + s)
          self.situationBudgetsTab.setItem(j, 1, situation)

          
          
          # formulaire pour ajouter un budget
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
          layout.addWidget(self.situationBudgetsTab)
          layout.addWidget(dateLabel)
          layout.addWidget(lineEdit1)
          layout.addWidget(montantLabel)
          layout.addWidget(lineEdit2)
          layout.addWidget(addButton)

          # affichage de ce layout
          self.tabBudgets.setLayout(layout)

     
     
     def majBudget(self, nomBudget: QLineEdit, montantMax: QLineEdit):
          self.budgetsTab.setRowCount(self.budgetsTab.rowCount() + 1)
          self.situationBudgetsTab.setRowCount(self.situationBudgetsTab.rowCount() + 1)
          
          # # ajout du budget dans le fichier Budget.txt
          self.budgets.addBudgetInFile(nomBudget, montantMax)

          # rangement des valeurs dans le tableau des situations
          for k in range(len(self.dicoBudgets)-1):
               
               nom = QTableWidgetItem(self.dicoBudgets[k][0])
               # rangement de la valeur à la position courante
               self.situationBudgetsTab.setItem(k, 0, nom)

               s = str(self.dicoBudgets[k][1])

               # on veut savoir à combien nous sommes de la limite de budget fixée
               situation = QTableWidgetItem("0" + "/" + s[:-1].strip())
               # rangement de la valeur à la position courante
               self.situationBudgetsTab.setItem(k, 1, situation)
               
          k = len(self.dicoBudgets)-1
          
          # ajout du dernier élément en dur pas de '\n' ) supprimer
          nom = QTableWidgetItem(self.dicoBudgets[k][0])
          self.situationBudgetsTab.setItem(k, 0, nom)

          s = str(self.dicoBudgets[k][1])
          situation = QTableWidgetItem("0" + "/" + s)
          self.situationBudgetsTab.setItem(k, 1, situation)
          
          self.clearDico()
          # # mise à jour de l'affichage
          self.printBudgetsTab()
     
     
     
     def printBudgetsTab(self):
          
          # replisssage du dico avec les valeurs présentes dans le fichier
          self.remplirDico()

          # rangement des valeurs dans le tableau des budgets
          for i in range(len(self.dicoBudgets)):
               print(self.dicoBudgets)
               nom = QTableWidgetItem(self.dicoBudgets[i][0])
               self.budgetsTab.setItem(i, 0, nom)

               s = str(self.dicoBudgets[i][1])
               
               montantMax = QTableWidgetItem(s[:-1])
               self.budgetsTab.setItem(i, 1, montantMax)

          i = self.budgetsTab.rowCount()-1
               
          # ajout du dernier élément en dur pas de '\n' ) supprimer
          nom = QTableWidgetItem(self.dicoBudgets[i][0])
          self.budgetsTab.setItem(i, 0, nom)
          
          montantMax = QTableWidgetItem(str(self.dicoBudgets[i][1]))
          self.budgetsTab.setItem(i, 1, montantMax)

          return self.budgetsTab
     
     
     
     
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