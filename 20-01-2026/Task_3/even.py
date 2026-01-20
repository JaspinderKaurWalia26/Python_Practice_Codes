# 3.1 Even Number Finder: Write a program that takes a list of numbers. Use a for loop to iterate through the list. If a number is odd, print it. If you encounter the number 10, stop the loop.

list=[2,5,8,3,10,1,7]
for num in list:
    if(num%2!=0):
        print(num)
    elif(num==10):
        break