# Ask the user if they want to generate password or not
# If yes, ask for password length
# Generate password
# Print password
# If initial response is no, exit the program

import string
import random

# create a variable called character
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


# create a function signature
def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? (Yes/No):  ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program Ended")
    quit()
else:
    print("Invalid Input, please input Yes or No")
    quit()
