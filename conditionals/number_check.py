# Bohdana Vasylyshena
# Lab 4: Conditionals
# Part 2: Introduction to Conditionals
# Description: This program will compare two numbers, which user enterd. Also determines which is smaller or larger, or they are equal. It answers if the number is even or odd.


print("Welcome to the Number Comparison Program")
print("This program will compare two numbers, which user enterd. Also determines which is smaller or larger, or they are equal. It answers if the number is even or odd.")


# Question for the user input
num1 = int(input("Enter your first number (num1): "))
num2 = int(input("Enter your second number (num2): "))


# Compare num1 and num2
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")


# Optional bonus: if the number is even or odd
if num1 % 2 == 0:
    print(f"{num1} is even number.")
else:
    print(f"{num1} is odd number.")

if num2 % 2 == 0:
    print(f"{num2} is even number.")
else:
    print(f"{num2} is odd number.")
    
