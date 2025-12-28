import base64
import math
from operator import xor
import random
import hashlib
import string
import binascii
import morse
import nltk
import cryptography


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WORDS = ["apple", "banana", "carrot", "dog", "elephant", "fish", "giraffe", "hat", "ice", "joke", "kite", "lion", 
         "mouse", "nose", "orange", "pear", "queen", "rainbow", "star", "tree", "umbrella", "vase", "water", "xray", 
         "yarn", "zebra"]
SECRET_KEY = "copilot"
DELIMITER = "|"

def to_octal(c):
    return format(ord(c), "o")

def to_decimal(c):
    return str(ord(c))

def to_hexadecimal(c):
    return format(ord(c), "x")

def to_morse(c):
    codes = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
        "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.",
        ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.",
        ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
        "_": "..--.-", "\"": ".-..-.", "$": "...-..-", "@": ".--.-.", " ": "/"
    }
    
    morse.
    return codes.get(c.upper(), "")

def to_base36(n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sign = "-" if n < 0 else ""
    n = abs(n)
    result = ""
    while n:
        n, i = divmod(n, 36)
        result = digits[i] + result
    return sign + result or "0"

def to_binary(c):
    return format(ord(c), "b")

def to_sha256_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

def xor_encrypt(s, key):
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(s, key * len(s)))

def rotate_left(s, n):
    return s[n:] + s[:n]

def encode_message(message,):
    
    # Error handling
    if not message[0].isdigit():
        message = str(random.randint(1, 4)) + message
    set_number = int(message[0])
    
    
    if set_number == 1:
        
        codes = [to_octal(c) for c in message]
        
        codes = [str(int(code) - random.randint(1, 7)) for code in codes]
        
        symbols = [random.choice(ALPHABET) for digit in "".join(codes)]
        half = len(symbols) // 2
        
        symbols = symbols[half:] + symbols[:half]
        
        symbols = [random.choice(ALPHABET)] + symbols[:half] + [random.choice(ALPHABET)] + symbols[half:] + [random.choice(ALPHABET)]
        s = "".join(symbols)[::-1]
        s = to_sha256_hash(s) + s
        s = xor_encrypt(s, SECRET_KEY)
        n = random.randint(1, len(s))
        s = rotate_left(s, n) + str(n)
        s = DELIMITER.join([str(ord(c)) for c in s])
        
        return s
    
    elif set_number == 2:
        
        codes = [decimal(c) for c in message]
        
        primes = math.primes(100)
        
        codes = [str(int(code) * random.choice(primes)) for code in codes]
        
        codes = [base64(int(code)) for code in codes]
        
        codes = [code[::-1].zfill(4) for code in codes]
        
        letters = [random.choice(ALPHABET) for digit in "".join(codes)]
        random.shuffle(letters)
        
        s = "".join([random.choice(ALPHABET) + letter for letter in letters])
        s = s + hash(s)
        s = xor(s, SECRET_KEY)
        chunks = [s[i:i+4] for i in range(0, len(s), 4)]
        chunks[0], chunks[-1] = chunks[-1], chunks[0]
        s = "".join(chunks)
        return s

    elif set_number == 3:
        
        morse_list = []
        for char in message:
            morse_list.append(to_morse[char])
            
        word_list = []
        
        for morse in morse_list:
            word = ""
            for symbol in morse:
                if symbol == ".":
                    word += random.choice(WORDS)
                elif symbol == "-":
                    word += random.choice(WORDS)
            word_list.append(word)
        word_string = " ".join(word_list)
        
        chunk_list = []
        word_list = word_string.split()
        
        for i in range(0, len(word_list), 10):
            chunk = word_list[i:i+10]
            chunk.reverse()
            chunk_list.append(chunk)
        for chunk in chunk_list:
            chunk.insert(0, random.choice(WORDS))
            chunk.append(random.choice(WORDS))
            
        chunk_list.reverse()
        
        chunk_string = "\n".join([" ".join(chunk) for chunk in chunk_list])
        
        hash_string = hashlib.sha256(chunk_string.encode()).hexdigest()
        
        position = random.randint(0, len(chunk_string))
        
        chunk_string = chunk_string[:position] + hash_string + chunk_string[position:]
        
        encrypted_string = xor_cipher(chunk_string, secret_key)
        binary_list = []
        
        for char in encrypted_string:
            binary = bin(ord(char))[2:]
            binary = binary.zfill(8)
            binary_list.append(binary)
        binary_string = delimiter.join(binary_list)
        return list(binary_string)

    elif set_number == 4:
        
        hex_list = []
        
        for char in message:
            hex_list.append(hex(ord(char))[2:])
        hex_list = [hex[::-1].zfill(4) for hex in hex_list]
        letter_list = []
        
        for hex in hex_list:
            letter = ""
            for digit in hex:
                letter += random.choice(alphabet1)
            letter_list.append(letter)
        random.shuffle(letter_list)
        letter_string = ""
        
        for i in range(len(letter_list)):
            letter_string += letter_list[i]
            if i < len(letter_list) - 1:
                letter_string += random.choice(alphabet1)
        hash_string = hashlib.sha256(letter_string.encode()).hexdigest()
        letter_string += hash_string
        encrypted_string = xor_cipher(letter_string, secret_key)
        chunk_list = []
        
        for i in range(0, len(encrypted_string), 4):
            chunk = encrypted_string[i:i+4]
            chunk_list.append(chunk)
        chunk_list[0], chunk_list[-1] = chunk_list[-1], chunk_list[0]
        for chunk in chunk_list:
            chunk.insert(0, random.choice(list2))
            chunk.append(random.choice(list2))
        chunk_list.reverse()
        chunk_string = "\n".join([" ".join(chunk) for chunk in chunk_list])
        hash_string = hashlib.sha256(chunk_string.encode()).hexdigest()
        position = random.randint(0, len(chunk_string))
        chunk_string = chunk_string[:position] + hash_string + chunk_string[position:]
        encrypted_string = xor_cipher(chunk_string, secret_key)
        decimal_list = []
        for char in encrypted_string:
            decimal = str(ord(char))
            decimal_list.append(decimal)
        decimal_string = delimiter.join(decimal_list)
        return list(decimal_string)

    else:
        return ["Invalid set number"]
