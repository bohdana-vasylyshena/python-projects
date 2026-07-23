# Bohdana Vasylyshena
# Final Project
# Number Guessing Game
# Descriptions: That program will ask user for random number and saves high score to the file.

# Constants
FILE_NAME = "scores.txt"
LOW = 1
HIGH = 100

import random

# Load Score 
def load_scores():
    scores = []
    names = []
    


    try:
        infile = open(FILE_NAME, "r")

        for line in infile:
            line = line.strip()

            name, score = line.split(",") # Separate name and numbers
            names.append(name)
            scores.append(int(score))
            

        infile.close()
        return names, scores

    except:
        return names, scores
    

# Save the score 
def save_scores(names, scores):
    outfile = open(FILE_NAME, "w")

    for entry in scores:
        index = scores.index(entry)
        print(index)
        name = names[index]
        print(f"{name},{entry}\n")
        outfile.write(f"{name},{entry}\n")

    outfile.close()



# Update Score 
def update_scores(attempts, names, scores):
   
    print("\nGreat,you made the top-5 list!🎉")
    name = input("Enter your name: ")

    
    scores.append(attempts)
    names.append(name)

    
    return names, scores



# Show scores
def show_scores(names, scores):
    print("\n HIGH SCORES ")

    if len(scores) == 0:
        print("No scores right now, pleace play a game first!🎲")
    else:
        number = 1
        for i in range(len(scores)):
            print(f"{number}. {names[i]}, {scores[i]}")
            number += 1
    print("\n")



# Play game 
def play_game():
    number = random.randint(LOW, HIGH)
    attempts = 0
    guesses = []
    guess = 0

    print("\nI'm thinking of a number from 1 to 100.")
    print("Try to guess it!\n")

    while guess != number: 
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            guesses.append(guess)

            if guess > number:
                print("Too high.\n")
            elif guess < number:
                print("Too low.\n")

        except:
            print("Please enter a whole number.\n")

    print(f"\nCorrect! You guessed it in {attempts} attempts.")

    print("Your guesses were:")
    for num in guesses:
        if num == guesses [-1]:
            print(num)
        
        else:
            print(num,end= ",")

    return attempts



# Display menu
def display_menu():
    print("----- NUMBER GUESSING GAME -----")
    print("1. Play Game")
    print("2. View High Scores")
    print("3. Exit")
    print("--------------------------------")

    choice = int(input("Enter your choice (1-3): "))
    print()
    return choice




# Main function

def main():
   
    print("\n Welcome to the Number Guessing Game!🎯\n")

    names, scores = load_scores()
    choice = display_menu()

    while choice != 3:

        if choice == 1:
            attempts = play_game()

            # Check if score goes into top-5
            if len(scores) < 5:
                names, scores = update_scores(attempts,names,scores) 
                save_scores(names, scores) 


            else:
                # find worst score in top-5
                last_record = scores[-1]    
                     

                if attempts <= last_record:
                    scores = update_scores(attempts, names, scores)  
                    save_scores(names, scores)
                else:
                    print("\n Good job, but not enough for the top-5.\n")

            
        elif choice == 2:
            show_scores(names, scores)

    
        else:
            print("Invalid choice, please try again.\n")

        
        choice = display_menu()

    print("Thank you for playing the Game!🤝😊\n")

# Main function
main()

            