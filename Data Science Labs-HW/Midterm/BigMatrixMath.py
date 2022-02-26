# Numpy - BigMatrix Math
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 2/25/2022, DSCI 1302

import numpy as np

class BigMatrixMath:
  
  def __init__(self):
    self.list_matrix = []

  def __str__(self):
    return str(self.list_matrix)

  def addMatrix(self,array = np.random.randint(-70,159,(40,40))):
    self.list_matrix.append(array)

  def printDimension(self):
    for element in self.list_matrix:
      print(element.shape)

  def dotProductEligible(self,array1,array2):
    if array1.shape[1] == array2.shape[0]:
        return True
    return False


matrix1 = BigMatrixMath()
matrix_2 = np.array([[1,2],[1,2]])
matrix1.addMatrix(matrix_2)
matrix1.addMatrix()
matrix1.printDimension()

matrix_3 = np.array([[5,6,3,2,1,2],[1,4,3,6,3,4]])

matrix1.dotProductEligible(matrix_2,matrix_3)


  
    
  