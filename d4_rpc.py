# rock paper scissors w/ computer

import random

def rpc(choice):
    if choice == 0:
        return """
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """
    elif choice == 1:
        return """
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """
    elif choice == 2:
        return """
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """


choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
comp_choice_output = rpc(comp_choice)

print(f"{rpc(choice)}\n\nComputer chose:\n{comp_choice_output}")

if choice >= 3 or choice < 0:
    print("invalid, you lose.")
elif choice == 0 and comp_choice == 2:
    print("you win")
elif comp_choice == 0 and choice == 2:
    print("you lose")
elif comp_choice > choice:
    print("you lose")
elif choice > comp_choice:
    print("you win")
elif choice == comp_choice:
    print("you tied")
