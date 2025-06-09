#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names_f:
    names = names_f.readlines()

with open("./Input/Letters/starting_letter.txt") as start_letter_f:
    start_letter = start_letter_f.read()
    for name in names:
        stripped_name = name.strip() # strip of white space (including "\n")
        new_letter = start_letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as letter_to_send:
            letter_to_send.write(new_letter)