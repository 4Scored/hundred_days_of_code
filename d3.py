print("Welcome to Treasure Island.\nYour mission is to find the treausre.")
i1 = input("left or right? (left or right) ")
if i1 == "right": 
    print("Dead. Game Over.")
elif i1 == "left":    
    i2 = input("Encountered a lake. swim or wait? (swim or wait) ")
    if i2 == "swim": 
        print("Drowned. Game Over.")
    elif i2 == "wait":
        i3 = input("Found a door, but which? (red, blue, or yellow) ")
        if i3 == "red": 
            print("Game Over.")
        elif i3 == "blue":
            print("Game Over.")
        elif i3 == "yellow":
            print("You Win!")
        else:
            print("Wrong Answer. Game Over")    
    else:
        print("Wrong Answer. Game Over")
else:
    print("Wrong Answer. Game Over")