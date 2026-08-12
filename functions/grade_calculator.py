# Bohdana Vasylyshena
# Lab 8: Functions
# Part Two: Grade Calculator
# Descriptions: That program will count student score on an assignment and calculates both your percentage and letter grade.


# Constants
A_MINIMUM = 90
B_MINIMUM = 80
C_MINIMUM = 70
D_MINIMUM = 60
F_MINIMUM = 0

# Define main function
def main():
    print("Welcome to the Grade Calculator! \n ")
    total_points = int(input("Enter total possible points: "))
    score = int(input("Enter your score: "))

# Calculate percentage
    percentage = (score / total_points) * 100 

# Call get_letter_grade passing percentage as an integer
    letter_grade = get_letter_grade(int(percentage))

# Display results using proper f-strings
    print(f"\nYou scored {score:.1f} out of {total_points:.1f} points. ")
    print(f"Your percentage {percentage:.1f} %")
    print(f"Your letter grade {letter_grade:}")

def get_letter_grade(percentage):
    # Use if/elif/else to determine letter grade
    if percentage >= A_MINIMUM:
        return "A"  # Return the appropriate letter grade
    elif percentage >= B_MINIMUM:
        return "B"  
    elif percentage >= C_MINIMUM:
        return "C"  
    elif percentage >= D_MINIMUM:
        return "D"
    else:
        return "F"
    

# Call your main function

main()



