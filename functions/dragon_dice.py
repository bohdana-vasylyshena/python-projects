# Bohdana Vasylyshena
# Lab 9: More Functions
# Part 2: Dragon Dice Rolling
# Descriptions: That program will simulaterolling dragon dice and user can choose which die to roll and how many times


# Constants
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20

import random
# Function to roll on die
def roll(die_type):
    number = random.randint (1, die_type)
    return number

# Main function
def main():
    print ("Welcome to the Dragon Dice Rolling!\n ")    
    die_type = 1

    # Loop until 0 (ceycle need repied)
    while die_type != 0:     #until will be 0
        die_type = int(input("Which die type are you rolling (d4, d6, d8, d10, d12, d20)? "))

        if die_type == 0:
            print("You will stop rolling")

        elif die_type != D4 and die_type != D6 and die_type != D8 and die_type != D10 and die_type != D12 and die_type !=D20:    #if die correct
            print("Input not correct. Pleace enter 4, 6, 8, 10, 12, 20. \n ")

        else:
            total = 0 
            num_dice = int(input(f"How many {die_type} -sides dies would you like to roll? "))
            print ("You rolled: ",end= "")

            for i in range(num_dice):
               # print(f"i = {i}") # FOR MYSELF to know 
                rolled_value = roll(die_type)                
                if i == num_dice -1:
                    print (rolled_value)
                else:
                    print(f"{rolled_value},", end=' ')
            
                total += rolled_value


            
            print(f"\n Your total is:{total} \n")

    print(" Thank you for using this game! ")

# Main function
main()





