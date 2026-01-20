# 3.2 Vowel Skipper: Write a program that takes a string as input. Iterate through the string using a for loop. Print each character, but skip vowels (a, e, i, o, u).

text = input("Enter the string:")

for ch in text:
    if ch in 'aeiouAEIOU':
        continue
    print(ch)

    