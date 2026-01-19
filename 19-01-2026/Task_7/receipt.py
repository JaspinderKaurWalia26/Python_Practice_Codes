# 7.3 Receipt Generator: Write a program that takes a list of items and their prices as input, then uses f-strings to generate a formatted receipt.

items = []
prices = []

n = int(input("How many items needed? "))

for i in range(n):
    item = input(f"Enter item {i+1} name: ")
    price = float(input(f"Enter item {i+1} price: "))
    items.append(item)
    prices.append(price)

total = 0

for i in range(n):
    print(f"{items[i]:<15} ₹{prices[i]}")
    total = total + prices[i]


print(f"{'TOTAL':<15} ₹{total}")