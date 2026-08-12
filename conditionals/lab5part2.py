# Bohdana Vasylyshena
# Lab 5: More Conditionals
# Part Two: Flowchart Task
# Descriptions: This program will ask the user about three numbers (a,b,c), then compare them and give you a message about those numbers, using the statements.


print("Welcome to the number comparative program")
print("This program will ask the user about three numbers (a,b,c), then compare them and give you a message about those numbers, using the statements")


# Input
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))


# Flowchart Task 
if a > b:
    if a > c:
        print(f"Number a is selected: {a}")
    else: 
        print(f"Number c is selected: {c}")
else: 
    if b > c:
        print(f"Number b is selected: {b}")
    else:
        print(f"Number c is selected: {c}")
