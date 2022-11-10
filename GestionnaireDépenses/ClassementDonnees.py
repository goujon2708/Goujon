import sys
import pandas as pd
import numpy as np
from Depense import Depense

"""Class that carry out some treatments on the data
"""
class ClassementDonnees():

     def __init__(self):
         self.depenses = []
         
         
     """Get the column given for the file given with the path
     """
     def getDataColumn(self, path, column):
          data = pd.read_csv(path, sep=';')
          return data[column]

          """Adds all the expenses of the month given
          """
     def calculExpenses(self, path: str):
          return 0

          """Tidy datas in a Depense list
          """
     def tidyData(self, path):
          data = pd.read_csv(path, sep=';')
          for i in data.index:
               date = data["Date"][i]
               libelle = data["Libellé"][i]
               sortie = data["Débit euros"][i]
               entree = data["Crédit euros"][i]
               d = Depense(date, libelle, sortie, entree)
               self.depenses.append(d)

     
          """Print the list of depenses
          """
     def printList(self):
          for i in range(len(self.depenses)):
               element: Depense = self.depenses[i]
               print(element.getDate() + " " + 
                     element.getLibelle() + " " + 
                     str(element.getSortie()) + " " + 
                     str(element.getEntree())
                    )
     
          """add a depense to the list
          """
     def addDepense(self, date, libelle, sortie, entree):
          d = Depense(date, libelle, sortie, entree)
          self.depenses.append(d)


c = ClassementDonnees()
# c.getDataColumn("assets/files/octobre.csv", )
c.tidyData("assets/files/octobre.csv")
c.addDepense("01/01/01", "CHEESE NAAN WTF", "-7.00", "0")
c.printList()
