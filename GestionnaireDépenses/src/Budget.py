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
     def addBudget(self, nom, montantMax, situation):
          b = Budget()
          b.nom = nom
          b.montantMax = montantMax
          b.situation = situation
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
               print(elem.getNom() + " " + str(elem.getMontantMax()) + " " + str(elem.getSituation()))

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




b = Budget()
# b.addBudget("Nourriture", 120, 0)
# b.addBudget("Divers", 70, 0)

# print(b.getMontantMaxTab(1))
