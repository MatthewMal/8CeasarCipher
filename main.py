def encrypt(translation, offset):
    message = []
    for i in range(0, len(translation)):
        if translation[i] == " ":
            message.append(27)
        elif translation[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            message.append(int(translation[i]) + 28)
        else:
            message.append((alphabet.index(translation[i]) + offset) % 26)
    for j in range(0, len(message)):
        if message[j] == 27:
            message[j] = " "
        elif message[j] >= 28:
            message[j] = str(message[j] - 28)
        else:
            message[j] = alphabet[message[j]]
    print("".join(message))


def decrypt(translation, offset):
    message = []
    for i in range(0, len(translation)):
        if translation[i] == " ":
            message.append(27)
        elif translation[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            message.append(int(translation[i]) + 28)
        else:
            message.append((alphabet.index(translation[i]) - offset) % 26)
    for j in range(0, len(message)):
        if message[j] == 27:
            message[j] = " "
        elif message[j] >= 28:
            message[j] = str(message[j] - 28)
        else:
            message[j] = alphabet[message[j]]
    print("".join(message))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

do_again = True

while do_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
        do_we_continue = input("\nWould you like to re-run the program? Type 'yes' or 'no'\n")
        if do_we_continue != 'yes':
            do_again = False
    elif direction == "decode":
        decrypt(text, shift)
        do_we_continue = input("\nWould you like to re-run the program? Type 'yes' or 'no'\n")
        if do_we_continue != 'yes':
            do_again = False
    else:
        print("Please make sure your spelling is correct")
