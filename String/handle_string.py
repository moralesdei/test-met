#!usr/bin/env python
# encoding utf-8
# Prueba para la empresa MET GROUP 2020
# Punto No 1
# Deimer Andres Morales Herrera
import re

class MyString():
    def __init__(self, string):
        self.__string = string
        self.__flagOperation = False
        self.__resultOperation = 0;
    def operation(self):
        self.handleString()     
        print(self.__flagOperation)
      
    def compute(self):
         if self.__flagOperation:
            print(self.__resultOperation)

    def handleString(self):
         n = re.findall(r'[+-]?\d+', self.__string)
         if n:
            self.__flagOperation = True
            try:
              self.__resultOperation = eval(self.__string)
            except:
              self.__flagOperation = False
