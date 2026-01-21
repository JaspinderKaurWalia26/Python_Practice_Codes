# 1.1 Temperature Converter: Write a function called convert_celsius_to_fahrenheit that takes a Celsius temperature as a parameter and returns the equivalent Fahrenheit temperature. The formula is: Fahrenheit = (Celsius * 9/5) + 32.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*1.8)+32
    return fahrenheit

c=int(input("Enter the temperature in celsius:"))
print("Temperature in Fahrenheit:",convert_celsius_to_fahrenheit(c))

# 1.2 Area of a Rectangle: Write a function called calculate_rectangle_area that takes the length and width of a rectangle as parameters and returns its area. Provide default values for length and width (e.g., 1).
def calculate_rectangle_area(length,width):
    area=length*width
    return area

print("Area of rectangle:",calculate_rectangle_area(20,4))

# 1.3 String Reverser: Write a function called reverse_string that takes a string as a parameter and returns the reversed string.
def reverse_string(string):
    return string[::-1]

s=input("Enter the string:")
print("Reversed String:",reverse_string(s))   

# 1.4 Calculate Tip: Write a function called calculate_tip that takes the bill amount and tip percentage as parameters (with a default tip percentage of 15%). Return the tip amount. 
def calculate_tip(bill_amount,tip_percentage=15):
    tip=bill_amount*(15/100)
    return tip

Amount=int(input("Enter the Bill amount:"))
print("Tip Amount:",calculate_tip(Amount))
        
# 2.1 Area Calculation: Create a function called calculate_area that takes two arguments, length and width, and returns the area of a rectangle. Call the function with different values for length and width using both positional and keyword arguments.
def calculate_area(length,width):
    area=length*width
    return area

Positional=calculate_area(20,4)
print("Area calculated using Positional Argument:",Positional)
Keyword=calculate_area(width=4,length=20)
print("Area calculated using Keyword Argument:",Keyword)

# 2.2 List Modification: Create a function called add_item that takes a list and an item as arguments. The function should add the item to the end of the list. Test the function with different lists and items. Experiment with creating a copy of the list inside the function to avoid modifying the original list.
def add_item(list,item):
    newlist=list.copy()
    newlist.append(item)
    return newlist
    
list=[1,2,3,4]
print(add_item(list,5))


# 2.3 String Formatting: Create a function called format_address that takes three arguments: street, city, and state. The function should return a formatted address string in the following format: "{street}, {city}, {state}". Use keyword arguments when calling the function.
def format_address(street,city,state):
    address=f"{street},{city},{state}."
    return address

print(format_address(city="Ludhiana",state="Punjab",street="vishal nagar"))

# 2.4 Default Greeting: Modify the greet function from the examples to include a default greeting message (e.g., "Hello"). The function should take an optional greeting argument. If the greeting argument is not provided, it should use the default greeting message.

def greet(greeting="Hello"):
    greetings=f"{greeting}"
    return greetings

print(greet("Good Morning"))
print(greet())

# 3.1 Modify the Discount: Change the calculate_price function to accept the discount_rate as an argument instead of using a global variable. What are the advantages of doing this?
def calculate_price(discount_rate):
    return discount_rate

Actual_price=1500
print(calculate_price(1000))

# 3.2 Nested Function Challenge: Create a function called grandparent that contains two nested functions: parent and child. grandparent should have a local variable. The parent function should modify this variable using nonlocal, and the child function should print the modified value.

def grandparent():
    age=59
    def parent():
        nonlocal age
        age=41
    def child():
        print("Modified value:",age)
    parent()
    child()
grandparent()

# 3.3 Global Constant: Define a global constant PI = 3.14159. Write a function calculate_circle_area(radius) that uses this constant to calculate the area of a circle.

PI=3.14159
def calculate_circle_area(radius):
    area=PI*radius*radius
    return area

r=float(input("Enter the radius:"))
print(calculate_circle_area(r))
    
# 4.1 Temperature Conversion: Write a program that takes a temperature in Celsius as input from the user, converts it to Fahrenheit using the formula F = (C * 9/5) + 32, and prints the result. Use input(), float(), and print().

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*1.8)+32
    return fahrenheit

c=float(input("Enter the temperature in celsius:"))
print("Temperature in Fahrenheit:",convert_celsius_to_fahrenheit(c))

# 4.2 String Length and Reversal: Write a program that takes a string as input, prints its length using len(), and then prints the reversed string using reversed().

string=input("Enter a string:")
print(len(string))
reverse_string="".join(reversed(string))
print(reverse_string)

# 4.3 Finding the Range: Write a function that takes a list of numbers as input and returns the range (difference between the maximum and minimum values) of the numbers. Use max(), min(), and a return statement within the function.

def calculate_range(numbers):
    return max(numbers)-min(numbers)

num=[1,2,3,4]
print(calculate_range(num))

# 4.4 List to String: You have a list of characters. Create a single string from these characters using the str() function in a loop.

list=['h','e','l','l','o']
resulted_string=""
for element in (list):
    resulted_string=resulted_string+str(element)

print(resulted_string)

# 5.1 Area of a Trapezoid: Create a function calculate_trapezoid_area(base1, base2, height) that calculates the area of a trapezoid. The formula is: area = (base1 + base2) / 2 * height.

def calculate_trapezoid_area(base1, base2, height):
    area = (base1 + base2) / 2 * height
    return area

b1=float(input("Enter the base1:"))
b2=float(input("Entern the base2:"))
h=float(input("Enter the height:"))

print("Area:",calculate_trapezoid_area(b1,b2,h))

# 5.2 Area of a Square: Create a function calculate_square_area(side) that calculates the area of a square. The formula is: area = side * side.

def calculate_square_area(side):
    area=side*side
    return area

s=int(input("Enter the side of square:"))
print(calculate_square_area(s))

# 5.3 Combined Area: Create a function calculate_combined_area(rectangle_length, rectangle_width, circle_radius) that calculates the combined area of a rectangle and a circle. Use the previously defined functions calculate_rectangle_area and calculate_circle_area inside this function.

def calculate_combined_area(rectangle_length, rectangle_width, circle_radius):
    
    rectangle=calculate_rectangle_area(rectangle_length,rectangle_width)
    circle=calculate_circle_area(circle_radius)
    combined=rectangle+circle
    return combined
    
print(calculate_combined_area(1,1,1))

# 5.4 Error Handling: Modify the calculate_rectangle_area function to check if the length or width are negative. If either is negative, return an error message (a string) instead of calculating the area. You could return "Invalid input: Length and width must be positive."
    
def calculate_rectangle_area(length,width):
    if length<0 or width<0:
        return "Invalid input: Length and width must be positive."
    else:
        area=length*width
        return area
   
l=int(input("Enter the length:"))
w=int(input("Enter the width:"))
print(calculate_rectangle_area(l,w))


        
   
