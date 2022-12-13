import os

class Budget():
     
     def __init__(self) -> None:
          
          # nom du budget
          self.nom = ''
          # montant maximum du budget
          self.montantMax = 0
          # situation à l'instant T du budget
          self.situation = 0
          # liste de budgets
          self.budgets = []
          
     
     #############################
     # --- GETTERS & SETTERS --- #
     #############################

     def getNom(self):
          return self.nom    
     
     def setNom(self, nom):
          self.nom = nom
          
     def getMontantMax(self):
          return self.montantMax
     
     def setMontantMax(self, montant):
          self.montantMax = montant
     
     def getSituation(self):
          return self.situation
     
     def setSituation(self, situation):
          self.situation = situation

          
          
     """add a new budget to the list of budgets
     """
     def addBudget(self, nom, montantMax):
          
          b = Budget()
          b.nom = nom
          b.montantMax = montantMax
          self.budgets.append(b)
     
     """delete the budget given of list
     """
     def delBudget(self, nomBudget):
          
          for e in range(len(self.budgets)):
               elem: Budget = self.budgets[e]
               if(elem.getNom() == nomBudget):
                    self.budgets.remove(elem)
                    break
     
     """print the list
     """
     def printBudgets(self):
          
          for i in range(len(self.budgets)):
               elem: Budget = self.budgets[i]
               print(elem.getNom() + " " + str(elem.getMontantMax()))

     """return the list of budgets
     """
     def getBudgets(self):
          
          return self.budgets
     
     
     
     # méthodes permettant de retourner l'arrtibut voulu présent à la ligne 'row' de la liste des budgets

     def getNomTab(self, row):
          
          elem: Budget = self.budgets[row]
          return elem.getNom()
     
     def getSituationTab(self, row):
          
          elem: Budget = self.budgets[row]
          return elem.getSituation()
     
     def getMontantMaxTab(self, row):
          
          elem: Budget = self.budgets[row]
          return elem.getMontantMax()
     
     
     """récupère la liste des budgets et écrit son contenu dans un fichier .txt afin de faciliter la sauvegarde
     """
     def completeBudgetFile(self):
          
          # ouverture du fichier en écriture
          with open("Budgets.txt", "w") as budgetsFile:
               # écriture de l'élément (nom du budget) courant dans le fichier, ainsi que le montant max associé au budget
               for i in range(len(self.budgets)):
                    budgetsFile.write(f"{self.getNomTab(i)}\n{self.getMontantMaxTab(i)}\n")
               budgetsFile.close()
                    
     
     
     def addBudgetFromTxt(self):
          
          self.completeBudgetFile()
          with open("Budgets.txt", "r") as budgetsFile:
               ligne = budgetsFile.readline()
               nom = ligne
               while(ligne != ''):
                    print(ligne)
                    ligne = budgetsFile.readline()
                    montantMax = ligne
                    self.addBudget(nom, montantMax)
               budgetsFile.close()
     


     def addBudgetInFile(self, nom, montantMax):

          # si le fichier est vide, on ajoute à la première ligne du fichier
          if(os.path.getsize("Budgets.txt") == 0):
               budgetsFile =  open("Budgets.txt", "a")
               # écriture des 2 champs dans le fichier .txt, sur 2 lignes différentes
               budgetsFile.write(f"{nom} {montantMax}")
               budgetsFile.close()
               
          # sinon, il faut d'abord faire un retour chariot et ensuite ajouter les champs
          else:
               budgetsFile = open("Budgets.txt", "a")
               budgetsFile.seek(os.path.getsize("Budgets.txt"))
               # écriture des 2 champs dans le fichier .txt
               budgetsFile.write(f"\n{nom} {montantMax}")
               budgetsFile.close()
          
                    
               
          

############################
# Test de la classe Budget #
############################


# b = Budget()
# b.printBudgets()