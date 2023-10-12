#
# Problem statement:
#    
# Hide Assignment Information
# Instructions
# If you have a message you want to transmit securely, you can encrypt it (translate it into a secret code). 
# One of the simplest ways to do this is with a shift cipher. Famously, Julius Caesar used this type of 
# cipher when sending messages to his military commanders.
#
# We’ll call this number the encryption key. It is just the length of the shift we are using. For example,
# upon encrypting the message “cookie” using a shift cipher with encryption key 4, we obtain the 
# encoded message (or ciphertext): GSSOMI.
#
# Let’s consider the following conversion table for English alphabets: 
#
# Your challenge is to Implement the above shift cipher in Python. You are expected to write two 
# functions:
#
# • Encryption: An encryption function that takes the plain text and encryption key as an input and 
# returns the ciphertext as output.
#
#
# • Decryption: This function will take the output and encryption key of the above encryption function 
# and decode the message to give out the original plain text.
#
# Note: You are expected to handle only alphabetic inputs and white spaces for both your encryption 
# and decryption functions.
#
#
# Run instruction:
#        python script_name.py "YourMessageHere" 4 encrypt
#        python script_name.py "YourEncryptedMessageHere" 4 decrypt

import argparse

def encrypt(plain_text, key):
    """
    Encrypts the given plain_text using a shift cipher with the provided key.

    Args:
    - plain_text (str): The text to be encrypted.
    - key (int): The encryption key which determines the shift length.

    Returns:
    - str: The encrypted text (ciphertext).
    """
    
    encrypted_text = ""
    
    for char in plain_text:
        # If character is an alphabet.
        if char.isalpha():
            # Shift character within alphabet (uppercase or lowercase).
            shifted_char = chr(((ord(char) - 65 + key) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + key) % 26) + 97)
            encrypted_text += shifted_char
        # If character is whitespace or other character, add as it is.
        else:
            encrypted_text += char
            
    return encrypted_text

def decrypt(ciphertext, key):
    """
    Decrypts the given ciphertext using a shift cipher with the provided key.

    Args:
    - ciphertext (str): The text to be decrypted.
    - key (int): The encryption key which determines the shift length.

    Returns:
    - str: The decrypted text (plain text).
    """

    decrypted_text = ""
    
    for char in ciphertext:
        # If character is an alphabet.
        if char.isalpha():
            # Un-shift character within alphabet (uppercase or lowercase).
            shifted_char = chr(((ord(char) - 65 - key) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 - key) % 26) + 97)
            decrypted_text += shifted_char
        # If character is whitespace or other character, add as it is.
        else:
            decrypted_text += char
            
    return decrypted_text

def main():
    # Initialize the argument parser.
    parser = argparse.ArgumentParser(description="Shift cipher encryption and decryption.")

    # Add required arguments.
    parser.add_argument("message", type=str, help="The message to be encrypted or decrypted.")
    parser.add_argument("key", type=int, help="The encryption key which determines the shift length.")
    parser.add_argument("action", choices=['encrypt', 'decrypt'], help="The action to be performed: encrypt or decrypt.")

    # Parse the arguments.
    args = parser.parse_args()

    if args.action == "encrypt":
        result = encrypt(args.message, args.key)
        print(f"Encrypted Message: {result}")
    elif args.action == "decrypt":
        result = decrypt(args.message, args.key)
        print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()