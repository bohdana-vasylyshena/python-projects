# Bohdana Vasylyshena
# Lab 7: More Loops
# Part Three: Budget Program From a Flowchart
# Description: This program will ask user for budget and expences and calculates them, depends how they are over,under or on budget


print("Welcome to the Mounthly Budget Calculator! \n ")

# Initialize variables
total_expenses = 0
expense = -1 # cycle need to start

# Ask about budget
budget = float(input("Enter your monthly budget: $"))

# Loop
while expense != 0:
    expense = float(input("Enter the expence value: $"))
    total_expenses = total_expenses + expense

difference = budget - total_expenses

# Results of budget
if total_expenses > budget:
    print(f"You are over budget $: {-difference:.2f}")
elif total_expenses < budget:
    print(f"You are under budger $: {difference:.2f}")
else:
    print("You are on budget! ")

print("Thank you for using that program! ")








