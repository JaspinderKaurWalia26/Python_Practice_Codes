# 2.3 Write a Python program to calculate the simple interest given the principal amount, rate of interest, and time period

def calculate(principal,roi,time):
    simple_interest=(principal*roi*time)/100
    return simple_interest

p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time period:"))

print(calculate(p,r,t))