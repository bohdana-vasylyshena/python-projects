# Bohdana Vasylyshena
# Lab 7: More Loops
# Part Two: Password Checking System
# Description: This program checks user's password and limits login attempts.

# Welcome message
print("-- Welcome to our Password Checking System -- \n")

# Constants
CORRECT_PASSWORD = "DANA"
MAX_ATTEMPTS = 5

# Counter
attempts = 1
password = input("Enter password: ")
attempts_left = MAX_ATTEMPTS 
# Loops
while password != CORRECT_PASSWORD and attempts < MAX_ATTEMPTS:
    attempts_left = MAX_ATTEMPTS - attempts
    print(f"Incorrect password. You have {attempts_left} attempts left.")
    password = input("Enter password: ")
    attempts = attempts + 1
    
if password == CORRECT_PASSWORD:
    print("Correct password. Welcome!")
else:
    print("Your account is locked. Too many incorrect attempts!")
    password = CORRECT_PASSWORD   
    