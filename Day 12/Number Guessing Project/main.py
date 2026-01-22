import random
from art import logo

def welcome():
    """Welcome user, print logo and greetings"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def play(difficulty):
    # pick a random number between 1 and 100
    number = random.choice(range(1, 101))
    attempts = 10 if difficulty == 'easy' else 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    # ask for a number while there are attempts left and the number hasn't been guessed
    guess = int(input("Make a guess: "))
    while attempts > 0:
        attempts -= 1
        # if number is guessed then show "You got it! The answer was [number]."
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return True
        # if user's guess is greater than the number picked
        elif guess > number:
            # show "Too high." and attempts left as in previous case
            print("Too high.")
        # if user's guess is less than the number picked
        elif guess < number:
            # show "Too Low" and attempts left "You have [] attempts remaining to guess the number.
            print("Too low.")
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
        # ask for a new guess
        guess = int(input("Make a guess: "))
    return False

continue_playing = 'y'
while continue_playing == 'y':
    welcome()
    # ask user to select the game's difficulty
    difficultyOpt = input("Choose a difficulty. Type 'easy' or 'hard':")
    guessed = play(difficultyOpt)
    # if number is not guessed and user runs out of attempts show "You've run out of guesses. Refresh the page to run again."
    if guessed == False:
        print("You've run out of guesses.")
    continue_playing = input("Would you like to play again? (y/n): ")
