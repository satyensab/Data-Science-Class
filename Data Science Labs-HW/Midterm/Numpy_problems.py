# Numpy continued
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 2/25/2022, DSCI 1302
import numpy as np

#1. Create an array with values that are spaced linearly in a specified interval between 0.0 100.0 as a numpy.float64, over 25 values
array1 = np.linspace(0.0,100.00,25,dtype = np.float64)
print(array1)

#2.Given the following arrays show me a line where I can combine the values into a larger array
a = np.array([[56, 12], [39, 74]])
b = np.array([[65, 76]])
c = np.append(a,b,0)
print(c)

#3.Whats a command to reformat a singular dimension array of 12 elements into a 3, 4 matrix.
d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(d)
reshaped_d = np.reshape(d,(3,4))
print(reshaped_d)






