# Bohdana Vasylyshena
# Lab 6: Loops
# Part One: Monkeys Jumping on the Bed
# Descriptions: The program counts down and prints the verses of a children's song about monkeys falling out of bed one by one.

# Question to User 
monkeys = int(input("How many monkeys start jumping on the bed? "))
print("\n")

# Loop 
for num in range (monkeys, 0, -1):
    print(f"{num} little monkeys jumping on the bed, 1 fell off and bumped his head, momma called the doctor and the doctor said, no more monkeys jumping on the bed.\n")

