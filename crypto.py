
"""
caser_Cipher

author: Hozyfa
"""

def caser_cipher(text, key, mode):
    result = ""
    for letter in text:
        if mode == "encrypt":
            result += chr(ord(letter) + (key % 25))
        elif mode == "decrypt":
            result += chr(ord(letter) - (key % 25))
    return result

def brute_force_decrypt(ciphertext):
    for key in range(1, 25):
        decrypted_text = caser_cipher(ciphertext, key, "decrypt")
        print(f"Key {key}: {decrypted_text}")

text = input("Enter the text: ")
key = input("Enter the key or type 'none' if unknown: ")
mode = input("Choose mode (encrypt/decrypt): ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode selection. Please choose 'encrypt' or 'decrypt'.")
else:
    if key.lower() == "none":
        print(" brute force decryption:")
        brute_force_decrypt(text)
    else:
        key = int(key)
        if mode == "encrypt":
            encrypted_text = caser_cipher(text, key, "encrypt")
            print(f"Encrypted text: {encrypted_text}")
        elif mode == "decrypt":
            decrypted_text = caser_cipher(text, key, "decrypt")
            print(f"Decrypted text: {decrypted_text}")







































