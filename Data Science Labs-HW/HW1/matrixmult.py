# Question 1
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 1/12/2022, DSCI 1302
import numpy as np

#a)
print("#a")
arr1= np.array([[0, 0, 1,0], [1, 0, 0, 0], [0, 1, 0, 0],[0,0,0,1]])
arr2 = np.array([[1],[2],[3],[4]])
arr3 = arr1.dot(arr2)
print(arr3)
print()

#b)
print("#b")
arr1b= np.array([[8,8,6]])
arr2b = np.array([[5,2],[1,3],[6,5]])
arr3b = arr1b.dot(arr2b)
print(arr3b)
print()

#c)
print("#c")
arr1c= np.array([[1,1],[2,0]])
arr2c = np.array([[0,2,3],[1,1,2]])
arr3c = arr1c.dot(arr2c)
print(arr3c)
print()