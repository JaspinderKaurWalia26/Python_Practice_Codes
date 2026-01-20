import random

play=input("Do you want to play:")
if (play!="yes"):
    print("Enter valid choice")
    play=input("Do you want to play:")
while play in ["Yes","yes"]:
    print("Level options=Easy,Medium,Hard")
    level=input("Enter the level:")
    if level=="Easy":
        lower_bound=1
        upper_bound=10
    elif level=="Medium":
        lower_bound=1
        upper_bound=100
    elif level=="Hard":
        lower_bound=1
        upper_bound=1000
    else:
        print("Enter valid choice")
        break
    
    number=random.randint(lower_bound,upper_bound)
  # print(number)
    max_guess=7
   
    while max_guess>0:
        guess=int(input("Enter the number:"))
        if (guess>upper_bound or guess<lower_bound):
            print("Invalid guess,chance consumed")
        elif (guess==number):
            print("Correct guess")
            break
        else:
            if (guess<number):
                print("Enter Higher Number")
            else:
                 print("Enter lower Number")

        max_guess=max_guess-1
        
        if max_guess==0:
            print("You lost the game")
            print("Number",number)
            play=input("Do you want to play again(yes/no):")
    
#if (play!="yes"):
#   print("Enter valid choice")
#   play=input("Do you want to play:")
print("Thanks for playing.")
    
      

    