import random
import os
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    card_choice = random.choice(cards)
    return card_choice

def computer_hidden_cards():
    computer_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    return

def choose_cards():
    user_cards.append(deal_cards())
    user_cards.append(deal_cards())
    user_total = sum(user_cards)
    computer_hidden_cards()
    print(f"Your cards: {user_cards}, current score: {user_total}")
    print(f"Computer's first card: {computer_cards[0]}")
    carry_on = True
    computer_total = sum(computer_cards)
    if user_total == 21 and computer_total == 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        print("It's a draw")
        return
    elif user_total == 21 and computer_total < 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        print("Blackjack!!!! You WIN")
        return
    if computer_total == 21 and user_total < 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        print("You lose :(")
        return
    elif user_total < 21:
        while carry_on:
            another_card = input("Do you want to choose another card? Type 'y' or 'n': ")
            if another_card == "y":
                user_cards.append(deal_cards())
                user_total = sum(user_cards)
                if user_total == 21:
                    print(f"Your cards: {user_cards}, current score: {user_total}")
                    carry_on = False
                if user_total > 21:
                    if 11 in user_cards:
                        index = user_cards.index(11)
                        user_cards[index] = 1
                        user_total = sum(user_cards)
                        print(f"Your cards: {user_cards}, current score: {user_total}")
                        print(f"Computer's first card: {computer_cards[0]}")
                    else:
                        print(f"Your final hand: {user_cards}, final score: {user_total}")
                        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
                        print("You lose :(")
                        return
                else:
                    print(f"Your cards: {user_cards}, current score: {user_total}")
                    print(f"Computer's first card: {computer_cards[0]}")
            elif another_card == "n":
                carry_on = False

    if computer_total < 17:
        computer_choosing = True
        while computer_choosing:
            computer_cards.append(deal_cards())
            computer_total = sum(computer_cards)
            if computer_total == 21:
                computer_choosing = False
            elif computer_total > 21:
                computer_choosing = False
            elif computer_total >= 17:
                computer_choosing = False

    if user_total == computer_total:
        print(f"Your final hand: {user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        print("It's a draw.")
        return
    elif user_total > computer_total:
        print(f"Your final hand: {user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        print("You win!!!")
        return
    elif user_total < computer_total > 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        print("You win!!!")
        return
    elif user_total < computer_total:
        print(f"Your final hand: {user_cards}, final score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        print("You lose :(")
        return
    return

play = False
start = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
if start == "y":
    play = True
while play:
    print(logo)
    user_cards = []
    computer_cards = []
    choose_cards()
    play = False
    restart = input("Do you want to play another game?")
    if restart == "y":
        os.system('cls')
        play = True
else:
    play = False
