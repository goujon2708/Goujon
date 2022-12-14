import pandas as pd
import os
from Depense import Depense



"""Class that carry out some treatments on the data
"""
class Data():

     def __init__(self):
          
          # liste de dépenses
          self.depenses = []
          # liste de mois
          self.mois = []


     def getDepenses(self):
          
          return self.depenses



     def getMois(self):
          
          return self.mois

  

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

          self.depenses.clear() # to avoid copies
          # lecture du fichier présent au chemin passé en paramètre
          data = pd.read_csv(path, sep=';')

          # rangement des données lues dans la liste des dépenses
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

 
     # méthodes permettant de retourner de récupérer l'attribut voulu présent à la ligne 'row' de la liste des dépenses

     def getDate(self, row):

          elem: Depense = self.depenses[row]
          return elem.getDate()

     def getLibelle(self, row):
          
          elem: Depense = self.depenses[row]
          return elem.getLibelle() 

     def getSortie(self, row):

          elem: Depense = self.depenses[row]
          return elem.getSortie()

     def getEntree(self, row):

          elem: Depense = self.depenses[row]
          return elem.getEntree()


     
     """add a depense to the list
     """
     def addDepense(self, date, libelle, sortie, entree):

          d = Depense(date, libelle, sortie, entree)
          self.depenses.append(d)



     """add a new month to the list
     """
     def addMonth(self, month):

          self.mois.append(month)



     """find the repo where all the files are stored et stores them in a list
     """
     def loadFile(self):
          
          # récupération du nom de tous les fichiers présents dans le répertoire passé en paramètre
          listFiles = os.listdir('C:/Users/arthu/OneDrive/Documents/GitHub/Goujon/GestionnaireDépenses/assets/files')
          
          # concaténation de la liste des fichiers présents dans le répertoire avec la liste des mois
          for i in range(len(listFiles)):
               
               self.mois.append(listFiles[i])


c = Data()
# c.getDataColumn("assets/files/octobre.csv")
#c.tidyData("../assets/files/octobre.csv")