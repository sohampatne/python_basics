# This is a python encoder and decoder that uses some creative techniques
# The encoder takes a message and returns a list of numbers
# The decoder takes a list of numbers and returns the original message
# The techniques used are:
# 1. Reversing the message
# 2. Shifting each character by its index
# 3. Converting each character to its ASCII code
# 4. Adding a random number between 1 and 10 to each code
# 5. Multiplying each code by its index
# 6. Adding the length of the message to each code
# 7. Swapping the first and last codes
# 8. Reversing the list of codes
# 9. Adding a checksum to the end of the list
# 10. Encrypting the list with a secret key

import random

# The secret key for encryption and decryption
secret_key = 123456789

# The encoder function


def encoder(message):
    # Reverse the message
    message = message[::-1]
    # Shift each character by its index
    message = "".join(chr((ord(c) + i) % 256) for i, c in enumerate(message))
    # Convert each character to its ASCII code
    codes = [ord(c) for c in message]
    # Add a random number between 1 and 10 to each code
    codes = [c + random.randint(1, 10) for c in codes]
    # Multiply each code by its index
    codes = [c * i for i, c in enumerate(codes)]
    # Add the length of the message to each code
    codes = [c + len(message) for c in codes]
    # Swap the first and last codes
    codes[0], codes[-1] = codes[-1], codes[0]
    # Reverse the list of codes
    codes = codes[::-1]
    # Add a checksum to the end of the list
    checksum = sum(codes) % 256
    codes.append(checksum)
    # Encrypt the list with the secret key
    codes = [c ^ secret_key for c in codes]
    # Return the list of codes
    return codes

# The decoder function


def decoder(codes):
    # Decrypt the list with the secret key
    codes = [c ^ secret_key for c in codes]
    # Check the checksum
    checksum = codes.pop()
    if checksum != sum(codes) % 256:
        return "Invalid checksum"
    # Reverse the list of codes
    codes = codes[::-1]
    # Swap the first and last codes
    codes[0], codes[-1] = codes[-1], codes[0]
    # Subtract the length of the message from each code
    length = len(codes)
    codes = [c - length for c in codes]
    # Divide each code by its index
    codes = [c // i for i, c in enumerate(codes)]
    # Subtract a random number between 1 and 10 from each code
    codes = [c - random.randint(1, 10) for c in codes]
    # Convert each code to its character
    message = "".join(chr(c % 256) for c in codes)
    # Shift each character by its index
    message = "".join(chr((ord(c) - i) % 256) for i, c in enumerate(message))
    # Reverse the message
    message = message[::-1]
    # Return the message
    return message
