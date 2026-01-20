"""
Guessing Game
Difficulty Levels: Modify the game to allow the player to choose between "Easy" (1-10), "Medium" (1-100), and "Hard" (1-1000) difficulty levels. Use if/elif/else statements to set the lower_bound and upper_bound variables based on the chosen difficulty.
Limited Guesses: Add a limit to the number of guesses the player can make (e.g., 7 guesses). If the player fails to guess the number within the limit, reveal the secret number and end the game. Use a while loop condition that checks both if the player has guessed correctly and if they have remaining guesses.
Play Again: After the game ends, ask the player if they want to play again. If they enter "yes" (or "y"), restart the game. Use a while loop to control whether the game continues to be played.
"""

import random

play=input("Do you want to play:")
if (play!="yes") and (play!="y"):
    print("Enter valid choice")
    play=input("Do you want to play:")
while play in ["Yes","yes","Y","y"]:
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
        continue
    
    number=random.randint(lower_bound,upper_bound)
 
    max_guess=7
   
    while max_guess>0:
        guess=int(input("Enter the number:"))
        if (guess>upper_bound or guess<lower_bound):
            print("Invalid guess,chance consumed")
        elif (guess==number):
            print("Correct guess")
            play = input("Do you want to play again (yes/no): ")
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
            play=input("Do you want to play again (yes/no):")
    

print("Thanks for playing.")
    
      

    