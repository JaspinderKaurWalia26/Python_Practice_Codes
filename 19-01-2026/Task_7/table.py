# 7.2 Table Formatter: Create a list of dictionaries, where each dictionary represents a person with keys like "name", "age", and "city". Use f-strings to format this data into a table-like output.

person=[
    {"name":"Aman","age":20,"city":"Ludhiana"},
    {"name":"Ansh","age":22,"city":"Patiala"},
    {"name":"Aman","age":20,"city":"Amritsar"}
]

print(f'{'Name':<10} {'Age':<5} {'City':<12}')
print("-"*30)

for p in person:
    print(f"{p['name']:<10} {p['age']:<5} {p['city']:<12}")
    
    
          