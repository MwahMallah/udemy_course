import caesar_functions as func

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    answer = func.encode(text, shift)
    print(answer)
elif direction == 'decode':
    answer = func.decode(text, shift)
    print(answer)
else:
    print("Choose 'encode' or 'decode'")