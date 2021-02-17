#!usr/bin/env python
# encoding utf-8
# Prueba para la empresa MET GROUP 2020
# Punto No 1
# Deimer Andres Morales Herrera
class MyMatrix():
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__countDimension = 0
        self.__sumMatrix = 0
        self.__flagStraight = True

    def dimension(self, multiList = None):
        if multiList is None:
          multiList = self.__matrix
        if type(multiList) is list:
          self.__countDimension += 1      
          self.dimension(multiList[0])
        # when multiList is not a list anymore, we can return the matrix dimension.       
        else:        
          print(self.__countDimension)
    
    def straight(self):
        self.__parsedMatrix()
        print(self.__flagStraight)

    def compute(self):
        self.__parsedMatrix()
        print(self.__sumMatrix)   

    def __parsedMatrix(self):
            self.__sumMatrix = 0
            if self.__countDimension == 1:
                self.__sumMatrix = sum(self.__matrix)
            elif self.__countDimension == 2:
                checkNumberElements = len(self.__matrix[0])
                for i in range(len(self.__matrix)):
                  self.__sumMatrix += sum(self.__matrix[i])
                  if(len(self.__matrix[i]) != checkNumberElements):
                    self.__flagStraight = False     
            # With this one, I check every dimension bigger than 2D.             
            else:   
                for i in range(len(self.__matrix)):
                  checkNumberElements = len(self.__matrix[i][0])
                  for j in range(len(self.__matrix[i])):
                      self.__sumMatrix += sum(self.__matrix[i][j])
                      if(len(self.__matrix[i][j]) != checkNumberElements):
                        self.__flagStraight = False
                

    

