# Bohdana Vasylyshena
# Programming Exercises 1
# Descriptions: That program will convert distance from kilometers to miles uses functions

# Constants
CONVERT = 0.6214

# Define main function

def main():
    print("Welcome to the Kilometer Converter! \n ")
    km = int(input("Enter a distance in kilometers: "))
    convert_to_miles(km)
    
def convert_to_miles(km):
    miles = km * CONVERT
    print(f"{km:.2f} kilometers the same as {miles:.2f} miles") 

# Call main functions
main()