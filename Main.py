# imports Libraries

import os
from cryptography import fernet

# Creates a List of all the item in the directory
files = os.listdir()

# List of files to protect
protected_files = ['Creater.py', 'Key_Gen.py', 'Key.key', 'Main.py']

# Opens and reads the Key
with open('Key.key', 'rb') as k:
    key = k.read()


def encrypt():
    for i in files:                                         # iterates through every file
        if i in protected_files:                            # checks if file is one of the protected files
            continue
        with open(i, 'rb') as f:                            # open the file in binary
            content = f.read()                              # reads the file in binary
            content = fernet.Fernet(key).encrypt(content)   # encrypts the content
        with open(i, 'wb') as f:                            # opens with writing privileges
            f.write(content)                                # Writes the encrypted content in binary


def decrypt():
    for i in files:                                         # iterates through every file
        if i in protected_files:                            # checks if file is one of the protected files
            continue
        with open(i, 'rb') as f:                            # open the file in binary
            content = f.read()                              # reads the file in binary
            content = fernet.Fernet(key).decrypt(content)   # decrypts the content
        with open(i, 'wb') as f:                            # opens with writing privileges
            f.write(content)                                # Writes the decrypted content in binary
