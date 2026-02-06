
def check(filename):
    try:
        file=open(filename,"r")
        contents=file.read()
        print(contents)
    except FileNotFoundError:
        print("Error: File not found creating a new one")
        open(filename,"w")
    finally:
        if file in locals() and not file.closed:
            file.close()
        print("Execution complete")
        
check("text.txt")