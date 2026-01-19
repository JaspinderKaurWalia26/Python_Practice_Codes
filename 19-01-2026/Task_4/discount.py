# 4.3 Write a Python program that checks if a user is eligible for a discount based on their age (under 18 or over 65) and membership status (must be a member)

def check(age,status):
    if (age<18 or age>65) and (status=="member"):
        print("Eligible for discount.")
    else:
        print("Not eligible for discount.")
        
a=int(input("Enter the age:"))
s=input("Enter the membership status:")
check(a,s)
