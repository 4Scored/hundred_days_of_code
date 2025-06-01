# number guessing

import random

ATTEMPTS = 0
number = random.randint(1,100)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
diff = input("Chosoe a difficulty. Type 'easy' or 'hard': ")

if diff == 'easy':
    ATTEMPTS = 10
elif diff == 'hard':
    ATTEMPTS = 5
print(f"You have {ATTEMPTS} attempts remaining to guess the number.")

won = False

while ATTEMPTS > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You go it! The answer was {number}")
        ATTEMPTS = 0
        won = True
    elif guess > number:
        print("Too high.\nGuess again.")
        ATTEMPTS -= 1
        print(f"You have {ATTEMPTS} attempts remaining to guess the number.")  
    elif guess < number:
        print("Too low.\nGuess again.")
        ATTEMPTS -= 1
        print(f"You have {ATTEMPTS} attempts remaining to guess the number.")    

if won == False:
    print("Ran out of lives, you lose.")
