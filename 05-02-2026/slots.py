import sys

# class without slots
class NormalStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# class with slots
class SlotStudent:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating objects
s1 = NormalStudent("Anil", 21)
s2 = SlotStudent("Anil", 21)

# Memory used by NormalStudent's __dict__ (stores attributes)
print("Memory of NormalStudent's __dict__:", sys.getsizeof(s1.__dict__))

# Memory used by SlotStudent object itself
print("Memory of SlotStudent object:", sys.getsizeof(s2))
