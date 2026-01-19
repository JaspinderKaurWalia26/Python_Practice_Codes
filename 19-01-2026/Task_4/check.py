# 4.2 Write a Python program that takes a year as input and checks if it is a leap year (divisible by 4, but not divisible by 100 unless also divisible by 400).

def check_leap_year(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        print("It's a Leap Year.")
    else:
        print("Not a leap year.")
        
y=int(input("Enter the year:"))
check_leap_year(y)

