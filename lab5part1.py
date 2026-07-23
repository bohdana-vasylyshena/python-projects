# Bohdana Vasylyshena
# Lab 5: More Conditionals
# Part One: Shipping Charges
# Descriptions: This program will calculate the shipping of a package based on weight, shipping method, and distance.


print("Welcome to Shipping Charges Calculator")
print("This program will calculate the shipping of a package based on weight, shipping method, and distance.")


# Constants
NEXT_DAY_MILE_RATE = 0.66    # per mile
TWO_DAY_MILE_RATE = 0.45     # per mile


# User input
weight = int(input("Enter the package weight in pounds: "))
print("Choose your shipping method:")
print("1 = 1-Day")
print("2 = 2-Day")
method = int(input("Enter 1 or 2: "))
distance = int(input("Enter the distance in miles: "))


# Base rate 
if method == 1:    # 1-Day
    if weight <= 5:
        base_rate = 12.50
    elif weight <= 20:
        base_rate = 18.00
    elif weight <= 50:
        base_rate = 26.00
    else:
        base_rate = 32.50
    mileage_fee = NEXT_DAY_MILE_RATE * distance
    method_name = "1-Day"

elif method == 2:  # 2-Day
    if weight <= 5:
        base_rate = 8.75
    elif weight <= 20:
        base_rate = 11.50
    elif weight <= 50:
        base_rate = 20.50
    else:
        base_rate = 25.00
    mileage_fee = TWO_DAY_MILE_RATE * distance
    method_name = "2-Day"
else: 
    print("Invalid shipping method selected!")
    exit()


# Total Cost
total_cost = base_rate + mileage_fee


# Output Receipt
print("\n---- SHIPPING RECEIPT ----\n")
print(f"Package Weight: {weight:.2f} lbs")
print(f"Shipping Method: {method_name}")
print(f"Ditance: {distance} miles")
print(f"Base Rate:       ${base_rate:,.2f}")
print(f"Mileage Fee:     ${mileage_fee:,.2f}")
print("\n__________________________")
print(f"Total Cost:      ${total_cost:,.2f}")



