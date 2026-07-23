# Bohdana Vasylyshena
# Lab 6: Loops
# Part Four: Multiplication Tables
# Descriptions: That program will displays a multiplication table for a number chosen by the user.

# Friendly message what the program does
print("This program will show you the multiplications table for any number from 1 to 12. ")

# Ask the user to enter a whole number between 1 and 12
number = int(input("Enter a whole number between 1 and 12: "))

# Loop
for num in range(1,11):

    # Result 
    result = number * num

    # Display each multiplication fact
    print(f"{number} x {num} = {result}")
    