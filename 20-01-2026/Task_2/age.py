# 2.1 Age Checker: Write a program that asks the user for their age. If the age is less than 13, print "You are a child." If the age is between 13 and 19 (inclusive), print "You are a teenager." Otherwise, print "You are an adult."

def check(age):
    if(age<13):
        print("You are a child")
    elif(age>=13 and age<=19):
        print("You are a teenager")
    else:
        print("You are an adult.")
        
a=int(input("Enter the age:"))
check(a)

      