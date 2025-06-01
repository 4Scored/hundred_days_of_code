# ceasar cipher

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''def encrypt(og_text, shift_amt):
    shifted_str = ""
    for letter in og_text:
        if letter in alphabet:
            shifted_pos = alphabet.index(letter) + shift_amt
            shifted_pos %= len(alphabet) # accounts for shifting beyond the length of the alphabet  
            shifted_str += alphabet[shifted_pos] 
        else:            
            shifted_str += " "
    print(f"encoded text is: {shifted_str}")'''

'''def decrypt(og_text, shift_amt):
    shifted_str = ""
    for letter in og_text:
        if letter in alphabet:
            shifted_pos = alphabet.index(letter) - shift_amt
            shifted_pos %= len(alphabet) # accounts for shifting beyond the length of the alphabet  
            shifted_str += alphabet[shifted_pos] 
        else:            
            shifted_str += " "
    print(f"decoded text is: {shifted_str}")'''

def caesar(og_text, shift_amt, dir):
    shifted_str = ""
    if dir == 'decode':            
        shift_amt *= -1 # set it to subtract if we decode
    for letter in og_text:
        if letter not in alphabet:
            shifted_str += letter
        elif letter in alphabet:                        
            shifted_pos = alphabet.index(letter) + shift_amt            
            shifted_pos %= len(alphabet) # accounts for shifting beyond the length of the alphabet  
            shifted_str += alphabet[shifted_pos]         
    print(f"{dir}d text is: {shifted_str}")

print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print("cipher ending")
        exit() # end program
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    go_again_or_no = input("go again? 'yes' if so, 'no' to quit? ")
    if go_again_or_no == 'no':
        should_continue = False        
