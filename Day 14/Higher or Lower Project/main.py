from art import logo, vs
from game_data import data
from random import randint

"""
    1. get data
    2. pick 2 random characters
    3. make sure are different
    4. show Name, description and Country
    5. ask user to guess who has more followers
    6. compare number of followers in data and show message
        a. correct answer -> You're right! Current Score: {1 per each correct answer}
        b. incorrect answer -> Sorry, that's wrong. Final score: {}
    7. keep asking questions as long the user guess correctly
"""
def show_account_details(acct_details, name):
    print(f"Compare {name}: {acct_details['name']}, {acct_details['description']}, {acct_details['country']}.")

def get_random_number():
    return randint(0, 50 -1)

def compare_followers(a, b):
    return a['follower_count'] > b['follower_count']

continue_playing = True
score = 0
while continue_playing:
    a = get_random_number()
    b = get_random_number()
    while a == b:
        b = get_random_number()
    acct_a = data[a]
    acct_b = data[b]
    print(logo)
    if score > 0:
        print(f"You're right! Current Score: {score}")
    show_account_details(acct_a, 'A')
    print(vs)
    show_account_details(acct_b, 'B')
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == "A":
        continue_playing = compare_followers(acct_a, acct_b)
    else:
        continue_playing = compare_followers(acct_b, acct_a)
    if continue_playing:
        score += 1

print(f"Sorry, that's wrong. Final score: {score}")