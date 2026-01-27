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
#Filling the rows and columns with 0 except the starting and ending rows/columns
border[1:-1,1:-1]=0
#Printing the array with internal values set to zero and border values set to one 
print(border)

"""
Task 4: Conditional Filtering Generate an array of 50 random integers between 1 and 100. Replace all odd numbers with -1 without creating a new array (in-place modification).
"""

#Generating an array
arr=np.random.randint(1,101,size=50)
#Replacing odd numbers with -1
arr[arr%2!=0]=-1
print(arr)

"""
Task 5: Finding the Nearest Value Create a 1D array of 20 random floats. Given a target value (e.g., 0.5), find the value in the array that is closest to that target and return its index.
"""

arr=np.random.random(20)
print(arr)
target=0.5
#Finding the index of closest array
index=np.abs(arr-target).argmin()
print("Index=",index)


"""
Task 6: The "Moving Average" Trend FinderMarketing data often has daily spikes. We use a moving average to see the real growth trend.The Task: Create an array representing 15 days of website traffic (e.g., [150, 160, 155, 180, 200...]).The Challenge: Calculate a 3-day moving average. The first result should be the average of days 1, 2, and 3; the second should be the average of days 2, 3, and 4, and so on.Hint: Look into np.cumsum or use clever slicing.
"""

web_traffic=np.array([150,160,155,180,200,190,220,200,165,170,210,175,185,225,220])
#Finding average using slicing
average=(web_traffic[:-2]+web_traffic[1:-1]+web_traffic[2:])/3
print(average)

"""
Task 7 : Image "Crop & Flip" Logic
"""

image=np.random.randint(0,256,(100,100,3))
cropped=image[25:75,25:75,:]
flipped=cropped[:,::-1,:]
print("Cropped Image Shape:",cropped.shape)
print("Flipped Image Shape:",flipped.shape)
