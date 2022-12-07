from cryptography.fernet import Fernet
 
# using the key
fernet = Fernet("Rd5r9UqYnmKdn7tO3Q6gw5AeohS4E584vKnZ0LX3lN8=")
 
# opening the encrypted file
with open('private copy for test.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('private copy for test.txt', 'wb') as dec_file:
    dec_file.write(decrypted)