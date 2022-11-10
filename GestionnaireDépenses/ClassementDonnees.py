import sys
import pandas as pd
import numpy as np

"""Class that carry out some treatments on the data
"""
class ClassementDonnees():

     """Get the column given for the file given with the path
     """
     def getDataColumn(self, path, column):
          data = pd.read_csv(path, sep=';')
          return data[column]
          
     """Adds all the expenses of the month given
     """
     def calculExpenses(self, path: str):
          return 0
     
     def tidyData(self, path):
          Depenses = []
          data = pd.read_csv(path, sep=';')
          print(data.shape)
          print(len(data))
          for i in len(data):
               print(data.loc[i])
          

c = ClassementDonnees()
c.tidyData("assets/files/octobre.csv")
