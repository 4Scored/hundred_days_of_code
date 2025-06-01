# higher or lower

import random
from info_data import data

still_alive = True
score = 0

print("/\ HIGHER OR LOWER \/")

choice_a = random.choice(data)

while still_alive:    
    choice_b = random.choice(data)
    while choice_b == choice_a:
        choice_b = random.choice(data)
    print(f"\nCompare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print("\nVS\n")
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
    decision = input("\nWho has more followers? Type 'A' or 'B': ")
    while decision not in ['A', 'B']:        
        decision = input("\nInvalid input. Please type 'A' or 'B': ")
        continue
    a_more = True
    if choice_b['follower_count'] >= choice_a['follower_count']:
        a_more = False
    if decision == 'A' and a_more:
        score += 1
        print(f"\nYou're right! Current score: {score}")
    elif decision == 'B' and not a_more:
        score += 1
        print(f"\nYou're right! Current score: {score}")
    elif decision == 'A' and not a_more:
        print(f"\nSorry, that's wrong. Final score: {score}")
        still_alive = False
    elif decision == 'B' and a_more:
        print(f"\nSorry, that's wrong. Final score: {score}")
        still_alive = False            
    choice_a = choice_b
    choice_b = random.choice(data)        
    print('\n\n\n')

