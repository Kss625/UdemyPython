''' Encryption method  '''


def encrypt(p_message, p_shiftNumber):
    cypher_message = ""
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_shiftNumber
            while new_position > 25:
                new_position = new_position - 26
            cypher_message = cypher_message + alphabet[new_position]
        else:
            cypher_message = cypher_message + char
    print(f"The Encode message is {cypher_message}")


'''Decryption'''


def decrypt(p_message, p_shift_number):
    cypher_message = ""
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - shift_Number
            while new_position < 0:
                new_position = new_position + 26
            cypher_message = cypher_message + alphabet[new_position]
        else:
            cypher_message = cypher_message + char
    print(f"The Encode Message is {cypher_message}")


enc_dec = input("Type E for Encrypt,type D for decrypt:\n")
end_program = False
while not end_program:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    message = input("Enter Your Message\n").upper()
    shift_Number = int(input("Enter the Shift Number:\n"))
    if enc_dec == "E":
        encrypt(message, shift_Number)
    else:
        decrypt(message, shift_Number)
    restart = input("Type 'Y' for continue and 'N' for not ontinue")
    if restart == "N":
        end_program = True
        print("See You Next Time")
