import sys
import pandas as pd
import numpy as np

"""Class that carry out some treatments on the data
"""
class ClassementDonnees():
     
     def __init__(self):
          pass

     """Get the column given for the file given with the path
     """
     def getDataColumn(path: str, column: str):
          data = pd.read_csv(path, sep=';')
          return data[column]
          
     """Adds all the expenses of the month given
     """
     def calculExpenses(self, path: str):
          return 0

