# Bohdana Vasylyshena
# Lab 8: Functions
# Part Three: Ingredient Adjuster Refactor
# This program can help you adapt an old family pancake recipe to the number that you want by using functions. 


# Function to calculateadjust ingredient amount
def adjust_ingredient(proportion, ingredient_amount):
    return proportion * ingredient_amount

# Main function
def main():

#Constants
    ALL_PURPOSE_FLOUR_GRAMS = 240        #grams of flour which needed for 8 pancakes
    SUGAR_GRAMS = 12.5                   #grams of sugar which needed for 8 pancakes
    BAKING_POWDER_GRAMS = 7              #grams of baking powder which needed for 8 pancakes
    MILK_MILLILITERS = 360               #milliliters of milk which needed for 8 pancakes
    LARGE_EGGS = 2                       #amount of large eggs which needed for 8 pancakes
    MELTED_BUTTER_GRAMS = 28             #grams of melted butter which needed for 8 pancakes
    VANILLA_EXTRACT_MILLILITERS = 5      #milliliters of vanilla extract which needed for 8 pancakes
    ORIGIONAL_PORTION = 8                #amount of pancakes in the original recipe
                 

#Message
    print("Welcome to the old family pancakes recipe converter. Choose your amount and enjoy!")


#Question about desired amount
    desired_amount_pancakes = int(input("How many pancakes do you want to make? "))


#Calculation desired amount to origional portion
    proportion = desired_amount_pancakes / ORIGIONAL_PORTION


#Calculation of new amount
    new_all_purpose_flour = adjust_ingredient(proportion, ALL_PURPOSE_FLOUR_GRAMS)
    new_sugar = adjust_ingredient(proportion, SUGAR_GRAMS)
    new_baking_powder = adjust_ingredient(proportion, BAKING_POWDER_GRAMS)
    new_milk = adjust_ingredient(proportion, MILK_MILLILITERS) 
    new_large_eggs = round(adjust_ingredient(proportion, LARGE_EGGS))  #round to whole number
    new_melted_butter = adjust_ingredient(proportion, MELTED_BUTTER_GRAMS)
    new_vanilla_extract = adjust_ingredient(proportion, VANILLA_EXTRACT_MILLILITERS)
   


#Adapted recipe
    print(f"Here is your recipe adapted to make {desired_amount_pancakes} pancakes:")
    print(f" {new_all_purpose_flour:.2f} grams of all-purpose flour")
    print(f" {new_sugar:.2f} grams of sugar")
    print(f" {new_baking_powder:.2f} grams of baking powder")
    print(f" {new_milk:.2f} milliliters of milk")
    print(f" {new_large_eggs} large eggs")
    print(f" {new_melted_butter:.2f} grams of melted butter")
    print(f" {new_vanilla_extract:.2f} milliliters of vanilla extract")
    print("I hope you liked the recipe. Thanks for joining my counter")

# Run program
main ()


