class Depense():
     
     def __init__(self, date, libelle, entree, sortie) -> None:
          
          # date de la dépense
          self.date = date
          # description rapide de la dépense
          self.libelle = libelle
          # montant du crédit si c'est une rentrée d'argent
          self.entree = entree
          # montant de la dépense
          self.sortie = sortie
          # catégorie de la dépense
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

# d = Depense("10/11/2022", "naan cheese", "0", "7")
# x = d.getDate()