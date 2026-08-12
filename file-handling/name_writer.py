# Bohdana Vasylyshena
# Lab 10: Files
# Part 2: Write Your Name
# Descriptions: That program will ask user their full name and then write it to the file.

# Main function
def main():
    FILE_NAME = "name.txt"
    print("This program will ask your name and then write the name to file. \n")

    full_name = input ("Write please your full name: ")

    try:
        outfile = open(FILE_NAME, 'w') # write file 

        outfile.write(f"{full_name}\n")

        outfile.close()
    
        print(f"\n Your name was written successfully to the file {FILE_NAME}.")

    except :
        print("ERROR: An error was written to the file.")


# Call main function
main()

