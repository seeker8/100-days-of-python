import random

from art import logo

def play(difficulty):
    attempts = 10 if difficulty == 'easy' else 5


# welcome user, print logo and greetings
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# ask user to select the game's difficulty
difficultyOpt = input("Choose a difficulty. Type 'easy' or 'hard':")


# pick a random number between 1 and 100
number = random.choice(range(1, 101))
attempts = 10 if difficultyOpt == 'easy' else 5
print(f"You have {attempts} attempts remaining to guess the number.")
# ask for a number while there are attempts left and the number hasn't been guessed
guess = int(input("Make a guess: "))
while attempts > 0:
    attempts -= 1
    # if number is guessed then show "You got it! The answer was [number]."
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
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

# if number is not guessed and user runs out of attempts show "You've run out of guesses. Refresh the page to run again."
if attempts == 0:
    print("You've run out of guesses. Refresh the page to run again.")
