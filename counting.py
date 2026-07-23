# Bohdana Vasylyshena
# Lab 6: Loops
# Part Two: Count by N 
# Descriptions: That program will ask user for a number and counts to 100 by that number.

# Message to the user
print("Let's count to 100")

# Prompt the user to enter a whole number
next_step = int(input("By what number do you wish to count? "))
print()
# Loop
for num in range( next_step,101,next_step):

# Output
 
 if num + next_step > 100:
  print (num)
 else:
  print(f"{num},", end=' ')