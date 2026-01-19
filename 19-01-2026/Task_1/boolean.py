# 1.4 Boolean Exercise: Write a program that checks if a number is both greater than 10 and less than 20. Print True if it is, and False otherwise. Test with the numbers 5, 15, and 25.

def check_number(num):
    return num>10 and num<20

print(check_number(5))
print(check_number(15))
print(check_number(25))
