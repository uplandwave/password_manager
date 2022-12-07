from cryptography.fernet import Fernet

# # key generation
# key = Fernet.generate_key()
 
# # string the key in a file
# with open('filekey.key', 'wb') as filekey:
#    filekey.write(key)

# # opening the key
# with open('filekey.key', 'rb') as filekey:
#     key = filekey.read()
 
# # using the generated key
# fernet = Fernet(key)
 
# # opening the original file to encrypt
# with open('private copy.txt', 'rb') as file:
#     original = file.read()
     
# # encrypting the file
# encrypted = fernet.encrypt(original)
 
# # opening the file in write mode and
# # writing the encrypted data
# with open('private copy.txt', 'wb') as encrypted_file:
#     encrypted_file.write(encrypted)

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

encrypt("private.txt","21XO0IS_MdgQm-WvSWdSB2YigtMuwMbVJw-qN7E_bfU=" )

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# decrypt("private.txt","21XO0IS_MdgQm-WvSWdSB2YigtMuwMbVJw-qN7E_bfU=" )