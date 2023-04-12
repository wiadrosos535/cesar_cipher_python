import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
def cesar(text, shift):
    encoded_communicate = ''
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)  
            encoded_communicate += alphabet[index + shift]
            print(encoded_communicate)        
        else:
            encoded_communicate += letter
            print(encoded_communicate)
            

game_start = True

while game_start :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cesar(text, shift)
    another_game = input("Would you like to go on type 'yes' or 'no':\n").lower
    if another_game == "no":
        game_start = False
                
   
