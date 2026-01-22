# 1.1 File Reader: Write a program that prompts the user for a filename and then opens the file in read mode. If the file exists, display its contents. If the file doesn't exist, display an error message.

f=input("Enter the filename:")

try:
    with open(f,'r') as file:
        contents=file.read()
        print(contents)
except FileNotFoundError:
    print("File not found")

# 1.2 File Writer: Write a program that prompts the user for a filename and then opens the file in write mode. Prompt the user to enter lines of text, and write each line to the file until the user enters "DONE".

f=input("Enter the filename:")
with open(f,'w') as file:
   #contents=input("Enter the contents for the file:")
    while True:
        line = input("")
        if line.lower()=="done":
            break

        else:
            file.write(line)
        
# 1.3 File Appender: Write a program that prompts the user for a filename and then opens the file in append mode. Prompt the user to enter lines of text to append to the file until the user enters "DONE"

f=input("Enter the filename:")
with open(f,'a') as file:
    while True:
        line = input()
        if "done" in line:
            break
        else:
            file.write(line)

   
# 1.4 Log File Creator: Create a simple log file creator. The program should ask the user for a log message and append it to a log file named app.log with a timestamp.

from datetime import datetime

message=input("Enter the log message:")
with open('app.log','a') as file:
    time=datetime.now()
    file.write(str(time)+"-"+message)
    
print("logs are saved")
    
    
# 2.1 Word Count: Write a Python script that reads a text file and counts the number of words in it. Assume words are separated by spaces. Consider how you would handle punctuation. Use the my_file.txt created earlier or create a new one with more text.

with open("test.txt","r") as file:
    text=file.read()
    text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    words=text.split()
    print(len(words))
    

# 2.2 Specific Line Retrieval: Write a function that takes a filename and a line number as input, and returns the content of that specific line in the file. Handle the case where the line number is out of range (i.e., greater than the number of lines in the file). Use readline() for this exercise.

def retrieval(filename, line_number):
    try:
        with open(filename, "r") as file:
            current_line = 1
            while True:
                line = file.readline()
                if not line:         
                    print("Line number out of range")
                    break

                if current_line == line_number:
                    print("Line content:", line)
                    break

                current_line =current_line + 1

    except FileNotFoundError:
        print("File not found")


f = input("Enter the name of the file: ")
n = int(input("Enter the line number: "))

retrieval(f, n)



# 2.3 Chunked Processing: Create a function that reads a large file in chunks of 1024 bytes and prints each chunk. This simulates how you might process very large files that cannot fit into memory all at once.

def read_in_chunks(filename):
    with open(filename, "rb") as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            print(chunk)

read_in_chunks("test.txt")

# 3.1 Create a program that takes user input and writes it to a file named user_input.txt. Each line of input should be written as a separate line in the file.

with open("user_input.txt", "w") as file:
    n = int(input("How many lines do you want to write? "))

    for i in range(n):
        line = input("Enter line: ")
        file.write(line + "\n")

# 3.2 Write a program that reads a list of names from the user and appends them to a file named names.txt. Ensure that the file is created if it doesn't exist.
with open("names.txt", "a") as file:
    print("Enter names (type STOP to finish):")
    while True:
        name = input()
        if name.lower() == "stop":
            break
        file.write(name + "\n")

# 3.3 Create a program that writes the numbers from 1 to 100 to a file named numbers.txt, each on a new line.

with open("numbers.txt","w") as file:
    for i in range(1,101):
        file.write(str(i)+"\n")

print("Numbers are written in the file")




