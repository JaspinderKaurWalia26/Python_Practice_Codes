# Optimizing loops and data structures

# Using list comprehension instead of loop

result=[i*i for i in range(5)]
print(result)

# Using set for faster lookup

numbers=set([1,2,3,4])
print(3 in numbers)

# Avoiding repeated calculation
import math
n=100
root=math.sqrt(n)
for _ in range(2):
    print(root)
    
# using enumerate

list=["a","b"]
for i,v in enumerate(list):
    print(i,v)


# Using zip for parallel loop

list1=[1,2,3]
list2=[4,5,6]
for x,y in zip(list1,list2):
    print(x+y)
    
# Prefer built in function

number=[1,3,5,7]
print(sum(number))

# choosing the right data structure 

from collections import deque
d=deque([1,2,3])
d.appendleft(0)
print(d)