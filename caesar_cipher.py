alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    encoded_text=""
    for letter in text:
        shift_pos=alphabet.index(letter)+shift
        shift_pos=shift_pos%26
        encoded_text+=alphabet[shift_pos]
    print("your encoded text is : ",encoded_text)


def decrypt(text,shift):
    decrypted_text=""
    for letter in text:
        shift_pos = alphabet.index(letter) - shift
        shift_pos = shift_pos % 26
        decrypted_text+= alphabet[shift_pos]
    print("Your decrypted text is : ",decrypted_text)

def controls(text,shift,direction):
    if direction=="encode":
        encrypt(text=text,shift=shift)
    elif direction=="decode":
        decrypt(text=text,shift=shift)
    else:
        print("Enter a valid direction")

path=""

while (path!="end"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    controls(text,shift,direction)
    option=input("Do you want to countinue type 'yes' else type 'no' ").lower()
    if option=="no":
        print("see you again! byeeee :) ")
        path="end"

