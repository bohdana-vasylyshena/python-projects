# Bohdana Vasylyshena
# Lab 4: Conditionals
# Part 3: Movie Ticket Price Calculator
# Description: This program for Binary Screen Cinema will help ticket sellers calculate the final price for movie tickets with special rate discounts for children and students.


print("Welcome to Binary Screen Cinema Ticket Calculator")
print("This program for Binary Screen Cinema will help ticket sellers calculate the final price for movie tickets with special rate discounts for children and students.")


# Constants
BASE_PRICE = 18.00               # Base ticket price
CHILD_DISCOUNT_RATE = 0.10       # Child discount rate 10%
STUDENT_DISCOUNT = 1.50          # Student discount 


# User input
age = int(input("Enter your age: "))                            # Customers age
student_id = input("Do you have a student ID? (y/n),(Y/N): ")      # Student ID


# Enter ticket price
ticket_price = BASE_PRICE


# Enter discounts
child_discount = 0.00
student_discount = 0.00


# Child discount if age < 13
if age < 13:
    child_discount = ticket_price * CHILD_DISCOUNT_RATE
    ticket_price = ticket_price - child_discount


# Student discount if student have ID
if student_id == "y" or student_id == "Y":
    student_discount = STUDENT_DISCOUNT
    ticket_price = ticket_price - student_discount



# Receipt for sellers and customers
print("TICKET CALCULATION")
print(f"Original Price: ${BASE_PRICE:.2f}")
print(f"Child Discount: -${child_discount:.2f}")
print(f"Student Discount: -${student_discount:.2f}")
print(f"Final Price: ${ticket_price:.2f}")


