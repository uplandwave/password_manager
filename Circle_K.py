import random
import csv
from cryptography.fernet import Fernet

def gen():
    print()
    amount = 16
    # amount = int(input("How many charecters do you want your password to be? "))
    pas_items = ["Q","W","E","R",'T','Y','U','I','O',
    'P','A','S','D','F','G','H','J','K','L','Z','X',
    'C','V','B','N','M','q','w','e','r','t','y','u',
    'i','o','p','a','s','d','f','g','h','j','k','l',
    'z','x','c','v','b','n','m','1','2','3','4','5',
    '6','7','8','9','0','!','@','#','$','%','^','&',
    '*','(',')','<','>','?',':','"',',','.','/',';']
    len = amount
    new_pass = []
    new_pass = (random.choices(pas_items, k = len))
    final_pass = (''.join(new_pass))
    print()
    print("New Password:", final_pass)
    print()
    return pas_items

def read_list(filename, key_column_index):
    dict_of_passwords = {}

    with open(filename, "rt") as pass_list:
        reader = csv.reader(pass_list)
        next(reader)

        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dict_of_passwords[key] = row
    return dict_of_passwords

def print_pass(dict_of_passswords):
    PASSWORD_INDEX = 1
    the_word = input("Witch of passwords would you like to see? ")
    item = dict_of_passswords[the_word]
    password = item[PASSWORD_INDEX]
    print()
    print(f"{the_word} password: {password}")
    print()
    return True

def add_new_item():
    new_site = input("What is the name of site you wish to add? ")
    new_pass = input("What is the new password? ")
    new_entry = f"{new_site},{new_pass}"
    with open("111/Week 12/private.txt", "a") as file_object:
        file_object.write("\n")
        file_object.write("\n")
        file_object.write(new_entry)
    print()
    print("New password added.")
    print()
    return False

def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)
    return True

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    return True

def main():
    SITE_INDEX = 0

    print()
    print("Welcome to Circle K")
    print("We are decripting your file now")
    print()
    decrypt("111/Week 12/private.txt","21XO0IS_MdgQm-WvSWdSB2YigtMuwMbVJw-qN7E_bfU=")
    first_choice = int(input("""Let me know wat you wnat to do.
    1) Generate new password
    2) Look at Vault
    3) Put in a new password
    4) Exit
    What would you like to do? """))
    while first_choice != 4:
        if first_choice == 1:
            gen()
            print()
            first_choice = int(input("""Now what do you want to do?
    1) Generate another new password
    2) Look at Vault
    3) Put in a new password
    4) Exit
    What would you like to do? """))
        elif first_choice ==2:
            pass_dict = read_list("111/Week 12/private.txt", SITE_INDEX)
            requested_password = print_pass(pass_dict)
            first_choice = int(input("""Let me know wat you wnat to do.
    1) Generate new password
    2) Look at another password
    3) Put in a new password
    4) Exit
    What would you like to do? """))
        elif first_choice ==3:
            add_new_item()
            first_choice = int(input("""Let me know wat you wnat to do.
    1) Generate new password
    2) Look at Vault
    3) Put in another password
    4) Exit
    What would you like to do? """))
        else:
            print()
            # print("Encripting your file now")
            # encrypt("private copy.txt","21XO0IS_MdgQm-WvSWdSB2YigtMuwMbVJw-qN7E_bfU=")
            # print("Good luck out there")
    print()
    print("Encripting your file now")
    encrypt("111/Week 12/private.txt","21XO0IS_MdgQm-WvSWdSB2YigtMuwMbVJw-qN7E_bfU=")
    print("Good luck out there")
    print()
    return first_choice

if __name__ == "__main__":
    main()