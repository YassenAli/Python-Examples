def encrypt_decrypt(message, mode):
    # mode is 1 to encrypt and -1 to decrypt
    encrypt = ''
    for char in message:
        if char.isspace():
            pass
        elif char.isalpha():
            if 65 <= ord(char) <= 90:
                char = chr(ord(char) + 32)
            if 97 <= ord(char) <= 122:
                encrypt += chr(ord(char) + mode)
        else:
            encrypt += char
    print(encrypt)
mode = 0
while (mode != 1) or (mode != -1):
    mode = input("please enter 1 to encrypt or -1 to decrypt: ")
    if (mode != 1) or (mode != -1):
        print("Invalid input!! Try again.")
if mode != 1:
    message = input("Please enter message to decrypt: ")
else:
    message = input("Please enter message to encrypt: ")
encrypt_decrypt(message, int(mode))
#             if encrypt[-1].isalpha():
#                 pass
#             elif encrypt[-1] == ('`' or '@'):
#                 encrypt[-1] = 'z'
#             elif encrypt[-1] == ('[' or '{'):
#                 encrypt[-1] = 'a'