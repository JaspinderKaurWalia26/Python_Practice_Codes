# 3.1 Write a Python program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

def check(a,b):
    if a>b:
        print(f'{a} is greater than {b}')
    elif a<b:
        print(f'{a} is less than {b}')
    else:
        print(f'{a} is equal to {b}')
        
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
(check(num1,num2)) 
