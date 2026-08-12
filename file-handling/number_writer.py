# Bohdana Vasylyshena
# Lab 10: Files
# Part 3: Number Accumulator
# Descriptions: That program will ask about positive numbers and then collect them to a file.

# Main Function
def main():
    FILE_NAME = "numbers.txt" 
    print ("Number Accumulator Program \n")
    print ("Enter positive numbers. Enter 0 when finished.\n")


    try:
        outfile = open(FILE_NAME, "w")      # file to write
        total_numbers = 0    # to stop

        number = float(input("Enter a number: "))

        while number != 0:     # while loop
            if number < 0:
                print ("Error: Only positive numbers allowed.\n")
            else:
                outfile.write(f"{number}\n")
                total_numbers += 1 # grow for 1 more
                print("Number recorded.\n")
            
            number = float(input("Enter a number: "))
            
        # Close file 
        outfile.close()

        print("Summary: ")
        print(f"Total number entered: {total_numbers}")
        print(f"Data saved to {FILE_NAME}")

    except ValueError:
        print("ERROR: An error was written to the file.")
    
# Main Function
main()
