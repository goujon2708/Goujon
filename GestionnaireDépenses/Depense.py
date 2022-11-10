class Depense():
     
     def __init__(self, date, libelle, entree, sortie) -> None:
          self.date = date
          self.libelle = libelle
          self.entree = entree
          self.sortie = sortie
          # self.categorie = categorie
     
     def getDate(self):
          return self.date
     
     def setDate(self, date):
          self.date = date
     
     def getLibelle(self):
          return self.libelle
     
     def setLibelle(self, libelle):
          self.libelle = libelle
          
     def getEntree(self):
          return self.entree
     
     def setEntree(self, entree):
          self.entree = entree
     
     def getSortie(self):
          return self.sortie
     
     def setSortie(self, sortie):
          self.sortie = sortie
     
     # def getCategorie(self):
     #      return self.categorie
     
     # def setCategorie(self, categorie):
     #      self.categorie = categorie

d = Depense("10/11/2022", "naan cheese", "0", "7")
x = d.getDate()
print(int(x[6:10]))