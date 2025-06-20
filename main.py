import os
#for clearing the terminal
def clear_console():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS/Linux
    else:
        os.system('clear')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  length=len(alphabet)
  for char in start_text:
    if char not in alphabet: 
       end_text+=char
    else:
        position=alphabet.index(char)
        if cipher_direction=='decode':
            new_postion=position-shift_amount
        elif cipher_direction=='encode':
            new_postion=(position+shift_amount)%length
        end_text += alphabet[new_postion]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
clear_console()
from art import logo
repeat=True
while repeat:   
    print(logo) 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    clear_console()
    print(logo)
    shift %=26;
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if choice =='no':
       repeat=False
       print("Goodbye")
    clear_console()
       
