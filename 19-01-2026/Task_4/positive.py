# 4.1 Write a Python program that takes three numbers as input and checks if all three numbers are positive.

def check(a,b,c):
    if a>0 and b>0 and c>0:
        print("All the three numbers are positive")
    else:
        print("All the three numbers are not positive")
        
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

check(a,b,c)
