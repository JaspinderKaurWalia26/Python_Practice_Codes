"""
2.3 Grade Calculator: Write a program that asks the user for their score on a test (out of 100). Assign a grade based on the following scale:
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
    Print the corresponding grade
"""

def grade_check(score):
    if(score>=90 and score<=100):
        print("Grade is A")
    elif(score>=80 and score<=89):
        print("Grade is B")
    elif(score>=70 and score<=79):
        print("Grade is C")
    elif(score>=60 and score<=69):
        print("Grade is D")
    else:
        print("Grade is F")
        
        
s=int(input("Enter the score:"))
grade_check(s)

      
        

    
    
    