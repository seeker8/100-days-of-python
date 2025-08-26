import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_opt = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
comp_opt = random.randint(0, 2)

#check for a valid input
if user_opt > 2 or user_opt < 0:
    print("Please choose a value among 0,1 or 2")

#print selected options
print(options[user_opt])
print(f"Computer chose:\n{options[comp_opt]}")

#print winner
if user_opt == comp_opt:
    print("Draw")
elif (user_opt > comp_opt and comp_opt != 0) or (user_opt == 1 and comp_opt == 0) or (user_opt == 0 and comp_opt == 2):
    print("You win")
else:
    print("You lose")

