# Calculator With History

import json
import datetime

def load_history():
    try:
        with open("history.json","r") as file:
            return json.load(file)
    except:
        return []
        
    
        
def save_history(record):
    with open("history.json","w") as file:
        json.dump(record,file,indent=4)
        
def calculator(operand_1,operand_2,operator):
    if operator=="+":
        return operand_1+operand_2
    elif operator=="-":
        return operand_1-operand_2
    elif operator=="*":
        return operand_1*operand_2
    elif operator=="/":
        if operand_2==0:
            return "Enter valid second number"
            #print("Enter valid number")
        else:
            return operand_1/operand_2
    else:
        print("Invalid ")
        
history=load_history()

while True:
    print("Calculator with history")
    print("1.Calculate\n2.Check saved history \n3.Exit")
    choice=input("Enter the choice:")
    if choice=="1":
        a=float(input("Enter first number:"))
        op=input("Enter operators(+,-,*,/):")
        b=float(input("Enter second number:"))
        result=calculator(a,b,op)
        print("Result=",result)
        
        record={
            "numbers":[a,b],
            "operator":op,
            "result":result,
            "time":datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        }
        history.append(record)
        save_history(history)
    elif choice=="2":
        for rec in history:
            print(rec)
    elif choice=="3":
        print("Exit")
        break
    else:
        print("Invalid choice")
        
        