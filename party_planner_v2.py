# Bohdana Vasylyshena
# Lab 9: More Functions
# Part One: Game Night Planning: Bonus
# Descriptions: That program will calculate how many pizza and beverages we need for the party 

# Constants
PIZZA_CUT_SLICES = 8
BEVERAGES_SOLD_PACKS = 6

def total_numbers(total_items, items_in_each_package):
    if total_items < items_in_each_package:
        packages = 1
    elif total_items % items_in_each_package == 0:
        packages = total_items //items_in_each_package

    else:
        packages = (total_items // items_in_each_package) + 1

    return packages


     # New Function
def leftovers(packages_needed, item_per_package, total_items_needed):
    leftovers_items = (packages_needed * item_per_package) - total_items_needed
    return leftovers_items

    
# Main function
def main():
    print("Welcome to Game Night Planning! \n ")
    guests = int(input("How many guests are you inviting? "))
    slices_per_guest = int(input("How many slices per guest? "))
    beverages_per_guest = int(input("How many beverages per guest? "))

    # Counting 
    total_slices = guests * slices_per_guest
    total_beverages = guests * beverages_per_guest

    # Functions pizza ans drinks
    pizza_needed = total_numbers(total_slices,PIZZA_CUT_SLICES)
    packages_needed = total_numbers(total_beverages,BEVERAGES_SOLD_PACKS)


    #  New Function for leftovers
    leftover_slices = leftovers(pizza_needed, PIZZA_CUT_SLICES, total_slices)
    leftover_cans = leftovers(packages_needed, BEVERAGES_SOLD_PACKS, total_beverages)

    # Output
    print(f"You will need to order {pizza_needed} pizza.")
    print(f"You will need to buy {packages_needed} 6-packs.")
    print("\n")
   

    # New Output for leftover
    print(f"You will need have {leftover_slices} leftover slices. ")
    print(f"You will need have {leftover_cans} leftover cans. ")
    print("\n")

    print("Thank you for using Game Night Planner!") 

main()