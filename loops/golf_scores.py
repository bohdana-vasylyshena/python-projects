# Bohdana Vasylyshena
# Lab 7: More Loops
# Part One: Input Validation
# Descriptions: That program will validate the golf score and calculates whether the user's score is above or below par


# Message to the user
print("Welcome to Our Golf Course")
print("- - - - - - - - - - - - - - - - -")

# Constant for the par score
PAR_SCORE = 72

# Ask user about score
golf_score = int(input("Enter your golf score: " ))

# Loop
while golf_score < 18 or golf_score > 125:
    print("Score out of range [18-125]. ")
    golf_score = int(input("Enter your golf score: "))

difference = PAR_SCORE - golf_score
# Output
if golf_score > PAR_SCORE:
    print(f"You scored {-difference} over par.")
elif PAR_SCORE > golf_score:
    print(f"You scored {difference} under par.")
else:
    print(f"You scored par.")


    


