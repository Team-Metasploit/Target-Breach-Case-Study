#!/usr/bin/env python3

# Script:                   Python Metasploit
# Author:                   Courtney Hans
# Date of latest revision:  11/4/20
# Purpose:                  Encryption/Decryption tool for Windows

# Import libraries

from cryptography.fernet import Fernet
import os, math, time, datetime

# Declare variables

dir_count = 0
file_count = 0

# Declare functions

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    try:
        return open("key.key", "rb").read()
    except:
        return None

# function to write key only if it's not already there
def if_key():
    key = load_key()
    if key == None:
        key = write_key()
    return Fernet(key)

def encrypt_file():
    f = if_key()
    filename = input("Please enter the full filepath for the file you wish to encrypt? ")
    with open(filename, "rb") as file:
        #read file data
        file_data = file.read()
    # encrypt data
    encrypted_file = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_file)
    print(filename + " encrypted.")

def decrypt_file():
    f = if_key()
    filename = input("Please enter the full filepath for the file you wish to decrypt? ")
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_doc = file.read()
    #decrypt data
    decrypted_info = f.decrypt(encrypted_doc)
    # write the original file
    with open (filename, "wb") as file:
        file.write(decrypted_info)
    print(filename + " decrypted.")

def recurse_encrypt(filename):
    f = if_key()
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_file = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_file)

def recurse_decrypt(filename):
    f = if_key()
    with open(filename, "rb") as file:
        encrypted_doc = file.read()
    decrypted_info = f.decrypt(encrypted_doc)
    with open (filename, "wb") as file:
        file.write(decrypted_info)

#Traverse & encrypt directory tree
def print_dirContents_encrypt():
    global dir_count
    global file_count
    start_path = "C:/Users/IEUser/Desktop/CreditCardInfo"
    #start_path = input("Please enter the absolute path to the directory you want to encrypt: ")
    for (path,dirs,files) in os.walk(start_path):
        print('Directory: {:s}'.format(path))
        dir_count += 1
        #Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path,file))

            # Convert file size to MB, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                fsize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                fsize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                fsize = fstat.st_size
                unit = "B"

            mtime = time.strftime("%X %x", time.gmtime(fstat.st_mtime))

            # Print file attributes
            print('encrypting \t{:15.15s}{:8d} {:2s} {:18s}'.format(file,fsize,unit,mtime))
            file_count += 1
            filename = os.path.join(path,file)
            recurse_encrypt(filename)
            
    # Print total files and directory count
    print('\nEncrypted {} files in {} directories.'.format(file_count,dir_count))
    dir_count = 0
    file_count = 0    

#Traverse & decrypt directory tree
def print_dirContents_decrypt():
    global dir_count
    global file_count
    start_path = "C:/Users/IEUser/Desktop/CreditCardInfo"
    #start_path = input("Please enter the absolute path to the directory you want to decrypt: ")
    for (path,dirs,files) in os.walk(start_path):
        print('Directory: {:s}'.format(path))
        dir_count += 1
        #Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path,file))

            # Convert file size to MB, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                fsize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                fsize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                fsize = fstat.st_size
                unit = "B"

            mtime = time.strftime("%X %x", time.gmtime(fstat.st_mtime))

            # Print file attributes
            print('decrypting \t{:15.15s}{:8d} {:2s} {:18s}'.format(file,fsize,unit,mtime))
            file_count += 1
            filename = os.path.join(path,file)
            recurse_decrypt(filename)
            
    # Print total files and directory count
    print('\nDecrypted {} files in {} directories.'.format(file_count,dir_count))
    dir_count = 0
    file_count = 0 

# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
        Encryption tool: 
        1 - Recursively encrypt directory
        2 - Recursively decrypt directory
        3 - Encrypt a file
        4 - Decrypt a file
        5 - Exit
        Please enter a number: 
        """)

        if (mode == 1):
            print_dirContents_encrypt()
        elif (mode == 2):
            print_dirContents_decrypt()
        elif (mode == 3):
            encrypt_file()
        elif (mode == 4):
            decrypt_file()
        elif (mode == 5):
            break
        else:
            print("Invalid selection...")  
