# blackjack capstone

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def play_game():    
    game_in_action = True
    while game_in_action:
        player_cards = []
        comp_cards = []            
        for i in range(0,2):
            player_cards.append(get_card())
            comp_cards.append(get_card())

        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {comp_cards[0]}")
        another = input("Type 'y' to get another card, type 'n' to pass: ")
        if another == 'y':
            player_cards.append(get_card())
        
        if 11 in player_cards and sum(player_cards) > 21: # adjust for 11 if player_sum > 21
           player_cards[player_cards.index(11)] = 1
        if sum(comp_cards) < 17:
            comp_cards.append(get_card())     

        player_sum = sum(player_cards)
        comp_sum = sum(comp_cards)        

        print(f"     Your final score: {player_sum} and your final hand is {player_cards}")
        print(f"     Computer's final score: {comp_sum} and your final hand is {comp_cards}")

        if player_sum > 21 and comp_sum > 21:
            print("You lose. You went over 21.")  
        elif player_sum > 21:
              print("You lose. You went over 21.")
        elif comp_sum > 21:
             print("You win! Dealer went over 21.")  
        elif player_sum == comp_sum:
            print("You tied with the dealer")
        elif player_sum > comp_sum:
            print("You win!")
        else:
            print("You lose.")

        again = input("Do you want to play a game of Blackjack? Type 'y' play again, type 'n' to quit: ")
        if again == 'n':
            game_in_action = False



play_game()

    