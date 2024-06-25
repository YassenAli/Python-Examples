def encrypt_decrypt(message, mode):
    # mode is 1 to encrypt and -1 to decrypt
    encrypt = ''
    for char in message:
        if char.isspace():
            pass
        elif char.isalpha():
            if 65 <= ord(char) <= 90:
                encrypt += chr(((ord(char) - 65) + mode) + 65)
            if 97 <= ord(char) <= 122:
                encrypt += chr(((ord(char) - 91) + mode) + 91)
        else:
            encrypt += char
    print(encrypt)
mode = 0
while mode != (1 or -1):
    mode = int(input("please enter 1 to encrypt or -1 to decrypt: "))
    if mode != (1 or -1):
        print("Invalid input!! Try again.")
if mode != 1:
    message = input("Please enter message to decrypt: ")
else:
    message = input("Please enter message to encrypt: ")
encrypt_decrypt(message, mode)
