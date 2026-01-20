# List Methods 

list=["Python","is"]
# append method
list.append("easy")
print(list)

# clear method
newlist=[10,30,40,20]
newlist.clear()
print(newlist)

# copy method
l=list.copy()
print(l)

# count method
points=[10,3,4,2,1,3,3]
print(points.count(3))

# extend method
sentence=["Good","Morning"]
sentence.extend(points)
print(sentence)

# index method
i=points.index(3)
print(i)

# insert method
points.insert(2,20)
print(points)

print(points.pop(1))
print(points)


list.remove("is")
print(list)

list.reverse()
print(list)

scores=[12,2,10,5,1]
scores.sort(reverse=True)
print(scores)

list=[]