# 2.2 Write a Python program to convert Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32.
def conversion(celsius):
    fahrenheit=(celsius*1.8)+32
    return fahrenheit

c=int(input("Enter the temperature in celsius:"))
print(conversion(c))
