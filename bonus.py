# Bohdana Vasylyshena
# Lab 10: Files
# Part 4: Sales Data Summary (bonus)
# Descriptions: That program will read the numbers fromfile and calculates total, count and average and displays the summary.



# Constants
FILE_NAME = "sales_data.txt"
MONEY_TYPE = "$"

def get_average(total, count):
    average = total / count # result will be float
    return average

# Main Function
def main():
    print("Sales Data Summary Program. \n")


    try:
        infile = open(FILE_NAME, "r")     # Open to read
        total_sales = 0.0
        transactions = 0

        # Loop
        for line in infile:
            try:
                amount = float(line)
                total_sales += amount
                transactions += 1
            except ValueError:
                print("ERROR: Invalid data found.\n")


        # Closee file
        infile.close()

        # Calculate average 
        if transactions > 0:
            average = get_average(total_sales, transactions)
            
        else: 
            average = 0.0 # because float not integer

        print("Summary Report \n")
        print(f"Number of thansactions: {transactions}")
        print(f"Total Sales: {MONEY_TYPE}{total_sales:,.2f}")
        print(f"Average Order Value: {MONEY_TYPE}{average:,.2f}")

    except FileNotFoundError:
        print("ERROR: File was not found.")

# Call main function
main()
