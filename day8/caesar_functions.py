alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift):
    message = list(message)

    for num_letter, letter in enumerate(message):
        message[num_letter] = alphabet[alphabet.index(letter) + shift] 

    message = "".join(message)
    return message

def decode(message, shift):
    message = list(message)

    for num_letter, letter in enumerate(message):
        message[num_letter] = alphabet[alphabet.index(letter) - shift] 

    message = "".join(message)
    return message


