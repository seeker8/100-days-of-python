from functools import reduce
from art import logo
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_message = "\tComputer's first card: {computer_cards}"
user_message = "\tYour cards: {user_cards}, current score: {user_score}"
prompt_message = "Type 'y' to get another card, type 'n' to pass: "
prompt_continue = "Do you want to play a game of Blackjack? Type 'y' or 'n': "

def print_hands(score, hand, computer_hand):
    print(user_message.format(user_score=score, user_cards=hand))
    print(computer_message.format(computer_cards=computer_hand))

def print_final_hands(score, c_score, hand, computer_hand):
    final_score_message = "   Your final hand: {user_cards}, final score: {user_score}"
    final_computer_message = "   Computer's final hand: {computer_cards}, final score: {computer_score}"
    print(final_score_message.format(user_score=score, user_cards=hand))
    print(final_computer_message.format(computer_cards=computer_hand, computer_score=c_score))

def get_score(hand):
    aces = hand.count(11)
    score = reduce(lambda x, y: x + y, hand)
    tmp_score = 0
    if score > 21 and aces == 1:
        return score - 10
    elif score > 21 and aces > 1:
        return score - len(aces) * 10
    return score

if __name__ == "__main__":
    start_game_prompt = "Do you want to play a game of Balckjack? Type 'y' or 'n': "
    start_game = input(start_game_prompt)
    while start_game == "y":
        user_cards = [random.choice(cards) for i in range(2)]
        computer_cards = [random.choice(cards)]
        computer_score = get_score(computer_cards)
        user_score = get_score(user_cards)
        print(logo)
        print_hands(user_score, user_cards, computer_cards)
        keep_playing = 'y'
        while user_score < 21 and keep_playing == 'y':
            keep_playing = input(prompt_message)
            if keep_playing == "y":
                user_cards.append(random.choice(cards))
                user_score = get_score(user_cards)
                print_hands(user_score, user_cards, computer_cards)
            else:
                while 18 > computer_score < 21:
                    computer_cards.append(random.choice(cards))
                    computer_score = get_score(computer_cards)

        if user_score == 21:
            print_final_hands(user_score, computer_score, user_cards, computer_cards)
            print("Win with a Blackjack!")
            start_game = input(start_game_prompt)
        elif computer_score > 21:
            print_final_hands(user_score, computer_score, computer_cards, computer_cards)
            print("Opponent went over. You win")
            start_game = input(start_game_prompt)
        elif user_score > 21:
            print_final_hands(user_score,computer_score, user_cards, computer_cards)
            print("You went over. You lose")
            start_game = input(start_game_prompt)
        elif 21 - user_score < 21 - computer_score:
            print_final_hands(user_score, computer_score, user_cards, computer_cards)
            print("You win.")
            start_game = input(start_game_prompt)
        else:
            print_final_hands(user_score, computer_score, user_cards, computer_cards)
            print("You lose.")
            start_game = input(start_game_prompt)
