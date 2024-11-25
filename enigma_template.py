# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: YOUR_NAME_HERE
# created: MM.DD.YYYY
# last update:  MM.DD.YYYY

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using math
def encode_message():
    message = input("Enter the message to encode: ").lower()
    key = int(input("Enter the key (1-25): "))
    encoded_message = ""

    for char in message:
        if char in alphabet:
            new_index = (alphabet.index(char) + key) % 26
            encoded_message += alphabet[new_index]
        else:
            encoded_message += char

    print(f"Encoded message: {encoded_message}")

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    filename = input("Enter the filename to encode: ")
    key = int(input("Enter the key (1-25): "))

    try:
        with open(filename, 'r') as file:
            content = file.read().lower()

        encoded_content = ""
        for char in content:
            if char in alphabet:
                new_index = (alphabet.index(char) + key) % 26
                encoded_content += alphabet[new_index]
            else:
                encoded_content += char

        with open(f"encoded_{filename}", 'w') as file:
            file.write(encoded_content)

        print(f"File encoded successfully. Encoded file saved as 'encoded_{filename}'")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    filename = input("Enter the filename to decode: ")
    key = int(input("Enter the key (1-25): "))

    try:
        with open(filename, 'r') as file:
            content = file.read().lower()

        decoded_content = ""
        for char in content:
            if char in alphabet:
                new_index = (alphabet.index(char) - key) % 26
                decoded_content += alphabet[new_index]
            else:
                decoded_content += char

        with open(f"decoded_{filename}", 'w') as file:
            file.write(decoded_content)

        print(f"File decoded successfully. Decoded file saved as 'decoded_{filename}'")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key():
    try:
        filename = input("Enter the filename to decode: ")
        with open(filename, 'r') as file:
            content = file.read().lower()

        for key in range(1, 26):
            decoded_content = ""
            for char in content:
                if char in alphabet:
                    new_index = (alphabet.index(char) - key) % 26
                    decoded_content += alphabet[new_index]
                else:
                    decoded_content += char

            print(f"Key {key}: {decoded_content}")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[3.5] Decode unknown key\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "3.5":
            decode_unknown_key()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()
