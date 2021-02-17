#!usr/bin/env python
# encoding utf-8
# Prueba para la empresa MET GROUP 2020
# Punto No 1
# Deimer Andres Morales Herrera
from numpy import asarray

class MyMatrix():
    def __init__(self, matrix):
        self.__matrix = matrix;
        self.countDimension = 0;
    def dimension(self, multiList = None):
        if multiList is None:
          multiList = self.__matrix
        if type(multiList) is list:
          self.countDimension += 1
          self.dimension(multiList[0])       
        else:
          print(self.countDimension)
          return None

    def straight(self):
        pass

        
