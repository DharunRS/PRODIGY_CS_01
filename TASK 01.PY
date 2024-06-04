alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text,shift_key): #hello 123 h=7
    cipher_text=""
    for char in plain_text:                            #if decrypt shift_key=shift_key * -1
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text +=alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's is the text after encrytion: {cipher_text}")   

def decryption(cipher_text,shift_key): #khoor
    plain_text=""
    for char in cipher_text: #char=k
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text +=alphabet[new_position]
        else:
            plain_text += char
    print(f"Here's is the text after decryption: {plain_text}") 

wanna_end=False
while not wanna_end:
    what_to_do=input("type 'encrypt' for encryption,type 'decrypt' for decryption:\n")
    text=input("type your message:\n").lower()
    shift=int(input("enter shift key:\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)
    play_again=input("type 'yes' to continue, type 'no' to exit.\n")
    if play_again=='no':
        wanna_end=True
        print("Have a nice day! Bye..")
