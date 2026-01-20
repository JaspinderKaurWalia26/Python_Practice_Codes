# 3.3 Positive Sum: Write a program that takes a list of numbers. Calculate the sum of only the positive numbers in the list. Use a for loop and the continue statement.
list=[3,-5,10,4]
sum=0
for item in list:
    if item>0:
        sum=sum+item
    else:
        continue
    
print(sum)