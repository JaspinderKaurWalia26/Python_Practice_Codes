# 6.1 Extracting Initials: Write a program that asks the user for their full name and extracts their initials using string slicing.

name=input("Enter the full name:")
s=name.split()
print(name)
print(s[0][0],s[1][0])