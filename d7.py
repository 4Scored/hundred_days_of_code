# hangman

import random

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']


lives = 6
chosen_word = random.choice(word_list)
print(f"chosen word is {chosen_word}")
print(HANGMANPICS[lives])

placeholder = ""
for i in range(0,len(chosen_word)):
    placeholder += "_"

game_over = False
correct_letters = []

while not game_over:
    guess = input("guess a letter: ").lower()
    
    displayholder = ""
    for letter in chosen_word:
        if guess == letter:
            displayholder += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            displayholder += letter          
        else:            
            displayholder += "_"            
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")     

    if '_' not in displayholder:
        game_over = True
        print("You Win!")     

    print(displayholder)
    print(HANGMANPICS[lives])