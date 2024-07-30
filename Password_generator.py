"""             Password Generator Task-3 Completed

A password generate is a useful tool that generate strong and random passwords for users. This project aims to create a 
password generate application using Python, allowing users to specify the lenght and complexity of the password.

User Input: Prompt the user to specify the desired lenght of the password.
Generate Password: Use a Combination of random characters to generate a password of the specified lenght.
Display the password: Print the generated password on the screen."""


import string
import random

def generate_password(Lenght,special_charts=False):
    characters = string.ascii_letters + string.digits
    if special_charts:
        characters +=string.punctuation # add punctuation value

        # to create a random choice in password lenght
    password= ''.join(random.choice(characters) for _ in range(Lenght))
    return password

def main():
    print("Password Generator")
    try:
        lenght=int(input("Enter the password lenght = "))
        special_characters = input("Include special character? y/n = ").lower()=='y'
        if lenght<=0:
            print("Password lenght should be a Positive Number:")
        else:
            password = generate_password(lenght,special_characters)
            print("Your Generated Password = ",password)
    except:
        print("Invalid Input")

if __name__=="__main__":
    main()