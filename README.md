# Python Projects — Bohdana Vasylyshena

A collection of Python programs I've built while learning Python: from early exercises with conditionals and loops to a final project with file storage and saved results.

## Project structure

```
basics/            first programs — variables, functions, simple input/output
conditionals/      if / elif / else practice
loops/             for and while loop practice
functions/         programs built around custom functions
file-handling/     reading from and writing to files
final-project/     the course's capstone project
```

## What's here

| File | Description |
|---|---|
| `basics/kilometer conv..py` | Converts kilometers to miles |
| `basics/Coffee (1).py` | Calculates savings from making coffee at home |
| `conditionals/number_check.py` | Compares two numbers, checks even/odd |
| `conditionals/tickets.py` | Movie ticket price calculator with discounts |
| `conditionals/lab5part1.py` | Shipping cost calculator |
| `conditionals/lab5part2.py` | Finds the largest of three numbers |
| `loops/counting.py` | Counts to 100 by a chosen step |
| `loops/monkeys.py` | Children's countdown song "Monkeys Jumping on the Bed" |
| `loops/multiplication.py` | Multiplication table for a chosen number |
| `loops/golf_scores.py` | Checks a golf score against par |
| `loops/password.py` | Password checking system with limited attempts |
| `loops/budget.py` | Monthly budget vs. expenses calculator |
| `functions/grade_calculator.py` | Calculates percentage and letter grade |
| `functions/ingredient_refactor.py` | Scales a pancake recipe to the desired amount |
| `functions/party_planner_v2.py` | Calculates how much pizza and drinks a party needs |
| `functions/dragon_dice.py` | Rolls tabletop-game dice (d4–d20) |
| `file-handling/name_writer.py` | Writes the user's name to a file |
| `file-handling/number_writer.py` | Collects entered numbers into a file |
| `file-handling/bonus.py` | Reads sales data from a file and summarizes it |
| `file-handling/to_do_list.py` | To-do list manager with file storage |
| `final-project/numberguess.py` | Final project: number guessing game with a high-score list |

## How to run

You only need Python 3 — everything uses the standard library, no external packages required.

```bash
git clone https://github.com/bohdana-vasylyshena/python-projects.git
cd python-projects
python3 "final-project/numberguess.py"
```

Programs that work with files (`file-handling/name_writer.py`, `file-handling/number_writer.py`, `file-handling/to_do_list.py`, `final-project/numberguess.py`) create their own `.txt` file next to the script when run from inside that folder. `file-handling/bonus.py` expects an existing `sales_data.txt` file in the same folder (one number per line).

## What I learned

Conditionals and loops (`while`, `for`), input validation, functions with parameters and return values, file I/O (reading/writing), working with lists, error handling with `try/except`, and string formatting with f-strings.

---

## Program details

### `basics/kilometer conv..py` — Kilometer to Miles Converter
An early exercise on functions: converts kilometers to miles.

```
$ python3 "kilometer conv..py"
Enter a distance in kilometers: 10
10.00 kilometers the same as 6.21 miles
```

### `conditionals/number_check.py` — Number Comparison
Compares two numbers to find which is larger, and checks each for even/odd.

```
Enter your first number (num1): 7
Enter your second number (num2): 4
7 is larger than 4.
7 is odd number.
4 is even number.
```

### `conditionals/tickets.py` — Movie Ticket Calculator
Calculates a movie ticket price with discounts for children under 13 and students.

```
Enter your age: 10
Do you have a student ID? (y/n),(Y/N): n
Original Price: $18.00
Child Discount: -$1.80
Student Discount: -$0.00
Final Price: $16.20
```

### `conditionals/lab5part1.py` — Shipping Cost Calculator
Calculates shipping cost based on package weight, shipping method (1-Day / 2-Day), and distance.

```
Enter the package weight in pounds: 10
1 = 1-Day
2 = 2-Day
Enter 1 or 2: 1
Enter the distance in miles: 50

---- SHIPPING RECEIPT ----
Base Rate:       $18.00
Mileage Fee:     $33.00
Total Cost:      $51.00
```

### `conditionals/lab5part2.py` — Largest of Three Numbers
Uses a flowchart-style comparison to find the largest of three entered numbers.

```
Enter the first number (a): 5
Enter the second number (b): 9
Enter the third number (c): 3
Number b is selected: 9
```

### `loops/golf_scores.py` — Golf Score Checker
Validates the score is within range (18–125) and shows how far it is above/below par (72).

```
Enter your golf score: 65
You scored 7 under par.
```

### `loops/password.py` — Password Checking System
Gives the user up to 5 attempts to enter the correct password.

```
Enter password: 1234
Incorrect password. You have 4 attempts left.
Enter password: DANA
Correct password. Welcome!
```

### `loops/budget.py` — Monthly Budget Calculator
Takes a budget and a list of expenses (0 to stop), then reports whether the user is over, under, or on budget.

```
Enter your monthly budget: $1000
Enter the expence value: $200
Enter the expence value: $300
Enter the expence value: $0
You are under budget $: 500.00
```

### `loops/counting.py` — Count to 100
Counts up to 100 using a step size entered by the user.

```
By what number do you wish to count? 25
25, 50, 75, 100
```

### `loops/monkeys.py` — Monkeys Jumping on the Bed
Prints the verses of the children's countdown song, one fewer monkey each time.

```
How many monkeys start jumping on the bed? 3
3 little monkeys jumping on the bed, ...
2 little monkeys jumping on the bed, ...
1 little monkeys jumping on the bed, ...
```

### `functions/dragon_dice.py` — Dragon Dice Roller
Lets the user pick a die type (d4, d6, d8, d10, d12, d20) and how many to roll, then sums the results.

```
Which die type are you rolling (d4, d6, d8, d10, d12, d20)? 6
How many 6-sides dies would you like to roll? 3
You rolled: 2, 5, 6
Your total is: 13
```

### `loops/multiplication.py` — Multiplication Table
Prints a multiplication table for a number from 1 to 12.

```
Enter a whole number between 1 and 12: 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

### `functions/grade_calculator.py` — Grade Calculator
Calculates percentage and letter grade (A–F) from a score and total possible points.

```
Enter total possible points: 100
Enter your score: 85
You scored 85.0 out of 100.0 points.
Your percentage 85.0 %
Your letter grade B
```

### `functions/ingredient_refactor.py` — Pancake Recipe Converter
Scales a family pancake recipe (originally for 8 pancakes) to any desired amount.

```
How many pancakes do you want to make? 16
480.00 grams of all-purpose flour
25.00 grams of sugar
...
```

### `functions/party_planner_v2.py` — Party Planner
Calculates how many pizzas and drink packs are needed for a party, and how much is left over.

```
How many guests are you inviting? 10
How many slices per guest? 3
How many beverages per guest? 2
You will need to order 4 pizza.
You will need to buy 4 6-packs.
```

### `basics/Coffee (1).py` — Coffee Savings Calculator
Calculates yearly savings from making coffee at home instead of buying it (260 cups/year).

```
Buying coffee at the cafe for one year will cost you: $1,235.00
Making coffee at home for one year will cost you: $221.00
You can save that amount of money: $1,014.00 by making your coffee at home.
```

### `file-handling/name_writer.py` — Name File Writer
Asks for the user's full name and writes it to `name.txt`.

```
Write please your full name: Bohdana Vasylyshena
Your name was written successfully to the file name.txt.
```

### `file-handling/number_writer.py` — Number Accumulator
Collects positive numbers (0 to stop) and saves them to `numbers.txt`.

```
Enter a number: 5
Enter a number: 10
Enter a number: 0
Total number entered: 2
Data saved to numbers.txt
```

### `file-handling/bonus.py` — Sales Data Summary
Reads numbers from `sales_data.txt` and calculates total, count, and average sales.

```
Number of thansactions: 5
Total Sales: $432.50
Average Order Value: $86.50
```

### `file-handling/to_do_list.py` — To-Do List Manager
Console task manager: view, add, and remove tasks, saved to `to_do_list.txt`.

```
1. View your to-do list
2. Add a task
3. Remove a task
4. Exit the program
Enter your choise from 1 to 4: 2
Enter your new task: Buy milk
Task Buy milk was added to the list
```

### `final-project/numberguess.py` — Number Guessing Game (Final Project)
The course's final project: the computer picks a number from 1–100, the player guesses it, and the top 5 scores are saved to `scores.txt`.

```
----- NUMBER GUESSING GAME -----
1. Play Game
2. View High Scores
3. Exit
Enter your choice (1-3): 1

I'm thinking of a number from 1 to 100.
Enter your guess: 50
Too high.
Enter your guess: 25
Too low.
Enter your guess: 37
Correct! You guessed it in 3 attempts.
```

