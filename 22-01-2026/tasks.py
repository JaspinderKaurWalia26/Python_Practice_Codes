# Build a Simple Student Grade Tracker

import statistics
grade_scale = "A-F"

def add_students(*names):
    return list(names)

def record_grades(**grades):
    return grades

def create_avg_calculator():
    total=0
    count=0
    def add_score(score):
        nonlocal total,count
        total=total+score
        count=count+1
        return total/count
        
    return add_score

def set_grade_scale(scale):
    global grade_scale
    grade_scale=scale

increase_grades=lambda grades:{name:grades+5 for name,grades in grades.items()}      

def top_students(grades_dict, threshold):
    stud_name=[name for name,grades in grades_dict.items() if grades>threshold]  
    return stud_name


changed_global=set_grade_scale("O-A-F")

student=add_students("Ankita","Arsh")
print("Student name:",student)

grades=record_grades(Ankita=78,Arsh=89)

print("The current grading scale:",grade_scale)
avg=create_avg_calculator()
updated_grades=increase_grades(grades)
top=top_students(updated_grades,85)
print(top)
overall_avg=statistics.mean(updated_grades.values())
print("Overall Average:",overall_avg)

print("Grades:",updated_grades)
print(avg(80))
print(avg(90))

