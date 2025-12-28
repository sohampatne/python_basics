'''This is a python encoder and decoder that uses some creative techniques
The encoder takes a message (in the form of user input) and returns a list of characters
The decoder takes a list of characters and returns the original message
The techniques used are:
Step 1: Converts each character to its hexadecimal code representation, which is a base-16 number system that uses 16 symbols (0-9 and A-F) to represent each byte of data. For example, the character ‘A’ is converted to ‘41’ in hex.
Step 2: Defines a set of 5 encoding and decoding methods in a list called ‘methods’. Each method is a function that takes a hex code and returns another hex code. The methods can be any mathematical or logical operations that are reversible. For example, one method could be adding 10 to the hex code, and another could be multiplying by 2. The index of the method used for each hex code is determined by the position of the hex code in the message. For example, the first hex code uses the first method, the second hex code uses the second method, and so on. The index of the method is then squared and subtracted by a variable integer x, and the result is appended to the end of the message. The variable x is a random number between 0 and the method index, and is also prepended to the start of the message. This step adds some randomness and complexity to the encoding and decoding process.
Step 3: Converts each hex code to its binary representation, which is a base-2 number system that uses 2 symbols (0 and 1) to represent each bit of data. For example, the hex code ‘41’ is converted to ‘01000001’ in binary. A variable integer y is then appended to the end of the binary message. The variable y is a random number between 0 and 1. If y is 0, all the digits in the binary message are reversed. If y is 1, no reversal is done. This step adds another layer of randomness and complexity to the encoding and decoding process.
Step 4: Splits the binary message into chunks of 8 bits, and replaces each chunk with a character from a predefined alphabet. The alphabet is a string of 256 characters that covers all the possible values of a byte. For example, the alphabet could be “abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_±=[]{};':,./<>?”. The character that corresponds to each chunk is determined by the decimal value of the chunk. For example, the chunk ‘01000001’ has a decimal value of 65, which corresponds to the character ‘A’ in the alphabet. This step converts the binary message into a more readable and compact form.
Step 5: Shuffles the alphabet randomly before each encoding and decoding, and uses the secret key as the seed for the shuffle. The secret key is a fixed integer that is known only to the encoder and decoder. The shuffle ensures that the same chunk of bits will not always map to the same character, and adds another layer of security and complexity to the encoding and decoding process.
Step 6: Joins the list of characters into a string, and inserts a random character from the alphabet between each pair of characters. For example, the string ‘ABC’ could become ‘A#B&C’, where ‘#’ and ‘&’ are random characters from the alphabet. This step adds some noise and length to the string, and makes it harder to recognize the original message.
Step 7: Rotates the string by a random number of steps, and appends the number of steps to the end of the string. For example, the string ‘A#B&C’ could be rotated by 2 steps to the right, and become ‘C&A#B2’. The rotation changes the order of the characters in the string, and makes it harder to decode the message.
Step 8: Encrypts the string with a secret key using a simple XOR cipher. The XOR cipher is a bitwise operation that takes two inputs and returns an output that is 1 if and only if the inputs are different, and 0 otherwise. For example, 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, and 1 XOR 1 = 0. The XOR cipher is applied to each character in the string and the secret key, and the result is another character from the alphabet. For example, if the secret key is 123, and the string is ‘C&A#B2’, the XOR cipher will produce ‘Z!T@N9’. The XOR cipher is a simple but effective way of encrypting and decrypting data, as it is reversible and requires the same secret key.
'''

import random
import string

secret_message = input(
    "Enter the secret message (all characters will be encoded/decoded): ")

# Encoding function


def encode(secret_message):

    # Step 1: Converts each character to its hexadecimal code representation
    hex_codes = [hex(ord(char))[2:].zfill(2) for char in secret_message]

    # Step 2: Defines a set of 5 encoding methods
    methods = ["add", "multiply", "reverse", "shuffle", "rotate"]

    # Step 3: Converts each hex code to its binary representation
    binary_messages = []
    for code in hex_codes:
        binary = bin(int(code, 16))[2:].zfill(8)
        binary_messages.append(binary)

    # Step 4: Splits the binary message into chunks of 8 bits
    encoded_messages = []
    for binary in binary_messages:
        encoded = ""
        for i in range(0, len(binary), 8):
            encoded += chr(int(binary[i:i+8], 2))
        encoded_messages.append(encoded)

    # Step 5: Shuffles the alphabet randomly
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};':,./<>?"
    random.shuffle(alphabet)
    shuffled_alphabet = "".join(alphabet)

    # Step 6: Joins the list of characters into a string
    encoded_string = ""
    for message in encoded_messages:
        encoded_string += message

    # Step 7: Inserts a random character from the alphabet between each pair of characters
    encoded_string = encoded_string.replace(
        "#", random.choice(shuffled_alphabet))

    # Step 8: Encrypts the string with a secret key
    encoded_string = "".join(chr(ord(char) ^ secret_key)
                             for char in encoded_string)

    return encoded_string


# Decoding function

def decode(encoded_string):

    # Step 1: Reverses the shuffle
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};':,./<>?"
    random.shuffle(alphabet)
    shuffled_alphabet = "".join(alphabet)
    encoded_string = encoded_string.replace("#", shuffled_alphabet)

    # Step 2: Decrypts the string with a secret key
    decoded_string = "".join(chr(ord(char) ^ secret_key)
                             for char in encoded_string)

    # Step 3: Splits the string into chunks of 8 bits
    decoded_messages = []
    for i in range(0, len(decoded_string), 8):
        decoded = decoded_string[i:i+8]
        decoded_messages.append(decoded)

    # Step 4: Joins the list of characters into a string
    decoded_string = ""
    for message in decoded_messages:
        decoded_string += message

    # Step 5: Converts each character to its hexadecimal code representation
    hex_codes = [hex(ord(char))[2:].zfill(2) for char in decoded_string]

    # Step 6: Converts each hex code to its original character
    decoded_message = ""
    for code in hex_codes:
        decoded_message += chr(int(code, 16))

    return decoded_message
