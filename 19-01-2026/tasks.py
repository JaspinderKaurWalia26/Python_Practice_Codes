# Program to print greetings and Square of a number.
def greet(name):
    print(f'Hello {name} I hope you are doing well!')
greet("Jaspinder")

def square(num):
    print(f'Square of {num} is:{num*num}')

num=int(input("Enter Number:"))
square(num)


# Program to make simple calculator 
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def division(a,b):
    return a/b

def multiply(a,b):
    return a*b

def modulus(a,b):
    return a%b

print(add(4,2))
print(subtract(4,2))
print(multiply(4,2))
print(division(4,2))
print(modulus(4,2))
