import sys
import random

sys.setExecutionLimit(1200000)

def guessing_game():  #To define the function for the guessing game
    random_int = random.randint(1, 100) #To generate a random integer between 1 and 100
    user_guess = int(input("Guess the number between 1 and 100(inclusive): ")) #To get the initial user guess
    attempts = 1 #To count the number of attempts
    while user_guess != random_int:
        attempts += 1
        
        #To provide feedback based on the user's guess
        if user_guess < random_int:
            user_guess = int(input(f"Sorry, {user_guess} is too low. Please try again.\nGuess the number between 1 and 101:  "))
        elif user_guess > random_int:
            user_guess = int(input(f"Sorry, {user_guess} is too high. Please try again.\nGuess the number between 1 and 101:  "))

    print(f"Congratulations! {user_guess} is the correct number! You guessed the number in {attempts} attempts!")                
guessing_game() #To call the guessing_game function to start the game
