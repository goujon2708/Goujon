class Bilan():
     def __init__(self) -> None:
          self.annee = ''
          self.entree = 0
          self.sortie = 0
          self.bilans = []
          pass

     def getAnnee(self):
          
          return self.annee
     
     def setAnnee(self, annee):
          self.annee = annee
     
     def getEntree(self):
          
          return self.entree
     
     def setEntree(self, entree):
          
          self.annee = entree
     
     def getSortie(self):
          return self.sortie
     
     def setSortie(self, sortie):
          
          self.sortie = sortie
     
     """add a bilan to the list of bilans
     """
     def addBilan(self, annee, entree, sortie):
          
          b = Bilan()
          b.annee = annee
          b.entree = entree
          b.sortie = sortie
          self.bilans.append(b)

     """delete the given bilan of the list
     """
     def delBilan(self, anneeBilan):
          
          for e in range(len(self.bilans)):
               
               elem: Bilan = self.bilans[e]
               if(elem.getAnnee() == anneeBilan):
                    self.bilans.remove(elem)
                    break
               
     """print the list of bilans
     """
     def printBilans(self):
          
          for i in range(len(self.bilans)):
               
               elem: Bilan = self.bilans[i]
               print(elem.getAnnee() + " " + str(elem.getEntree()) + " " + str(elem.getSortie()))

# b = Bilan()
# b.addBilan("2020", 2300, 2500)
# b.addBilan("2021", 4000, 3500)

# print("Avant suppression : ")
# b.printBilans()

# b.delBilan("2020")

# print("Après suppression : ")
# b.printBilans()