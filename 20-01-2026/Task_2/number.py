# 2.2 Number Classifier: Write a program that asks the user for a number. Determine if the number is positive, negative, or zero, and print an appropriate message.

def number_check(num):
    if(num==0):
        print("Number is zero")
    elif(num>0):
        print("Number is positive")
    else:
        print("Number is negative")

n=int(input("Enter the number:"))
number_check(n)
