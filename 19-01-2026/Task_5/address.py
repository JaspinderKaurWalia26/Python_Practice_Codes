# 5.3 Address Formatter: Ask the user for their street address, city, state, and zip code. Concatenate these inputs to create a properly formatted address string.

street_address=input("Enter the street addess:")
city=input("Enter the city:")
state=input("Enter the state:")
zip_code=input("Enter the zip code:")
address=street_address+" "+city+" "+state+" "+zip_code

print(f'{address}')