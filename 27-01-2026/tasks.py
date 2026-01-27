"""
Task 1: The Checkerboard Challenge
Create an 8*8 matrix and fill it with a checkerboard pattern (0s and 1s) using slicing only (no loops).
"""
# importing numpy library
import numpy as np
# Creating a checkboard with initially zeroes in 8*8 matrix
checkboard=np.zeros((8,8),dtype=int)
# Filling Even Rows and Odd Columns with 1
checkboard[::2,1::2]=1
# Filling Odd Rows and Even Columns with 1
checkboard[1::2,::2]=1
# Printing the final checkboard
print(checkboard)



"""
Task 2: Normalization Logic
Create a random 5*5 matrix. Calculate the mean and standard deviation. Then, "normalize" the matrix so that the data has a mean of 0 and a standard deviation of 1
"""

#Creating a random matrix of 5*5
matrix=np.random.rand(5,5)
#Calculating mean of matrix
mean=matrix.mean()
#Calculating standard deviation of matrix
std=matrix.std()
# Normalizing the matrix 
normalize=(matrix-mean)/std
# Printing the normalized matrix 
print(normalize)

"""
Task 3: Border Control
Create a 10*10 array of 1s. Change the internal values to 0 so that you are left with a "border" of 1s around the edges.
"""

#Creating a 10*10 array initially filled with 1s
border=np.ones((10,10),dtype=int)
#Filling the rows and columns with 0 except the starting and ending rows
border[1:-1,1:-1]=0
#Printing the array with internal values set to zero and border values set to one 
print(border)


