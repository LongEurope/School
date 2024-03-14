import os
import random
import time

#TODO account for blackjack hand

spades = []
diamonds = []
clubs = []
hearts = []
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [spades, diamonds, clubs, hearts]

player= []
dealer = []

def printlogo():
    print('88          88                       88        88                       88         ')
    time.sleep(0.1)
    print('88          88                       88        ""                       88         ')
    time.sleep(0.1)
    print('88          88                       88                                 88         ')
    time.sleep(0.1)
    print('88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   ')
    time.sleep(0.1)
    print('88P\'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    ')
    time.sleep(0.1)
    print('88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      ')
    time.sleep(0.1)
    print('88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   ')
    time.sleep(0.1)
    print('8Y"Ybbd8"\'  88 `"8bbdP"Y8  `"Ybbd8"\' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"\' 88   `Y8a  ')
    time.sleep(0.1)
    print('                                              ,88                                  ')
    time.sleep(0.1)
    print('                                            888P"                                  ')

def progress_bar(duration, actioning):
    prog_bar = '--------------------------------------------------------------------------------------------'
    interval = duration / len(prog_bar)
    for position in range(len(prog_bar) + 1):
        os.system('cls')
        print(f'|{prog_bar}|')
        print(f'{actioning}...')
        prog_bar = prog_bar[:position] + '█' + prog_bar[(position + 1):]
        time.sleep(interval)
    os.system('cls')

def get_answer(prompt, acceptable):
    while True:
        request = str(input(prompt)).lower()
        if request in acceptable:
            break
        else:
            print('Invalid input, please check the acceptable answers.')
    return request

def shuffle():
    for suit in deck:
        for rank in card_ranks:
            suit.append(rank)

def count(hand):
    total = 0
    for card_value in hand:
        if card_value == 'A':
            card_value = 11
        elif card_value == 'K' or card_value == 'Q' or card_value == 'J':
            card_value = 10
        else:
            card_value = int(card_value)
        total += card_value
    if total > 21:
        if 'A' in hand:
            total -= 10
    return total

def deal(hand):
    random_suit = random.choice(deck)
    random_card = random.choice(random_suit)
    random_suit.remove(random_card)
    hand.append(random_card)

def player_round():
    while True:
        action = get_answer(prompt='Would you like to hit or stand? H/S', acceptable=['h', 's'])
        if action == 's':
            break
        elif action == 'h':
            os.system('cls')
            deal(player)
            print(f'Dealer\'s hand: {random.choice(dealer)} and hole card, total: {count(player)}')
            print(f'Your hand: {player}, total: {count(player)}')
            if count(player) > 21:
                print('Bust')
                time.sleep(1)
                break

def dealer_round():
    os.system('cls')
    while count(dealer) < 21:
        deal(dealer)

def round_finish():
    os.system('cls')
    print(f'Dealer\'s hand: {dealer}, total: {count(dealer)}')
    print(f'Player\'s hand: {player}, total: {count(player)}')
    if count(player) > 21:
        if count(dealer) > 21:
            print('Push')
        else:
            print('Player bust, lose')
    else:
        if count(dealer) > 21:
            print('Dealer bust, win')
        else:
            if count(player) > count(dealer):
                print('Win')
            elif count(player) < count(dealer):
                print('Lose')
            elif count(player) == count(dealer):
                print('Push')

def shuffle_if_needed():
    card_count = 0
    for suit in deck:
        for card in suit:
            card_count += 1
    if card_count < 39:
        shuffle()

def main():
    printlogo()
    time.sleep(1)
    keep_playing = 'y'
    while keep_playing == 'y':
        os.system('cls')
        player.clear()
        dealer.clear()
        progress_bar(duration=0.4, actioning='shuffling')
        shuffle()
        progress_bar(duration=0.4, actioning='dealing cards')
        for _ in range(2):
            deal(player)
            deal(dealer)
        print(f'Dealer\'s hand: {random.choice(dealer)} and hole card')
        print(f'Your hand: {player}')
        player_round()
        progress_bar(duration=1.3, actioning='dealer\'s turn')
        dealer_round()
        round_finish()
        shuffle_if_needed()
        keep_playing = get_answer(prompt='Would you like to keep playing? Y/N: ', acceptable=['y', 'n'])
    os.system('cls')
    print('Thank you for playing')

main()