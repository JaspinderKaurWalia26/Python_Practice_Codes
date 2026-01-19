# 6.3 Palindrome Checker: Write a program that checks if a given string is a palindrome (reads the same forwards and backward) using string slicing.

string=input("Enter the string:")
if string == string[::-1]:
    print("Given string is a palindrome")
else:
    print("String is not a palindrome")
    
