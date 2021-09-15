# User Account Program
# Daniel Spiers 15/09/2021

"""
Create a program that allows a user to create a username and password.

- Only accept the password if it is at least 8 characters long and has both upper and lower case letters.

- Force the user to enter their password twice so that the computer knows that the user has not made any mistakes when typing their new password.

- When an acceptable password has been inputted, write the username and password to an external file named ‘users’

- Create a function that uses an algorithm to suggest how strong the password is (Weak, Medium, Strong) depending on the length, use of special characters and numbers.
"""


class User:

    # Sets up the user
    def __init__(self, username, password):

        users = open("users.txt", "r")

        if username + "~" in users.read():
            print("That username is already taken.")
            self.ok = False

        elif len(password) >= 8 and password.upper() != password and password.lower() != password and not ("~" in password):
            self.username = username
            self.password = password
            self.save()
            print("User Created Successfully.")
            self.ok = True
            
        else:
            print("Password isn't strong enough. Please make sure that password:\n>>> Contians Upper and Lower case letters\n>>> Is at least 8 characters long\n>>> Does not contain the ~ character")
            self.ok = False

        users.close()
    
    # Function to show a password's strength
    def passwordStrength(self):
        score = 0

        # Score for length of password
        if 10 <= len(self.password) <= 12:
            score += 1
        elif len(self.password) <= 20:
            score += 2
        else:
            score += 3
        
        # Score for use of numbers and special characters
        count = 0
        for i in self.password:
            if i in "1234567890":
                count += 1
        score += min(count, 1)

        # Score for use of special characters
        count = 0
        for i in self.password:
            if i in "@#!£$?":
                count += 1
        score += min(count, 4)

        return score
        

    # Adds the user to the users.txt file
    def save(self):
        users = open("users.txt", "a")
        users.write(f"{self.username}~{self.password}\n")
        users.close()

# Main loop
while True:
    user = input("Please input a username: ")
    pwd = input("Please input a password: ")
    pwd1 = input("Please re-input password: ")

    if pwd == pwd1:
        createdUser = User(user, pwd)
    else:
        print("Passwords didn't match")
        continue

    if createdUser.ok:
        print(f"Your password scored {createdUser.passwordStrength()} out of a maximum of 8.")

    again = input("Create another user? (y/n): ")
    if again != "y":
        break