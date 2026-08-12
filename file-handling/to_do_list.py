# Bohdana Vasylyshena
# Lab 11: Files & Lists
# Part 2 + 3: To-Do List Manager & File Storage
# Descriptions: That program will manage to do list and user can look the tasks, add and remove tasks. After that it will be saved in file.


# Constants
FILE_NAME = "to_do_list.txt"

# Main function 
def main():
    to_do_list = load_from_file()   # load from file

    choice = display_menu()

    while choice != 4:
        if choice == 1:
            view_list(to_do_list)
        elif choice == 2:
             to_do_list = add_task(to_do_list)
        elif choice == 3:
            to_do_list = remove_task(to_do_list)
        else:
            print("Your choice not correct")
        
        choice = display_menu()
    print("Thank you and Goodbye")

# Display menu for user
def display_menu():
    print("\n")
    print("To-Do List Manager")
    print("1. View your to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit the program") 
    choise = int(input("Enter your choise from 1 to 4: "))
    return choise



# View To-Do List
def view_list(to_do_list):
    print("To-Do List")

    if len(to_do_list) == 0:
        print("Your list is empty.")
    else: 
        index = 1
        for task in to_do_list:
            print(f"{index}.{task}")
            index += 1
        
# Add a task to list
def add_task(to_do_list):
    new_task = input("Enter your new task: ")
    to_do_list.append(new_task) # add to list
    print(f"Task {new_task} was added to the list")
    save_to_file(to_do_list) # save that after add
    return to_do_list

# Remove a task 
def remove_task(to_do_list):
    if len (to_do_list) == 0:
        print("Here no tast to remove.")
        return to_do_list
    else:
        view_list(to_do_list)
        number = int(input("Enter the task number which you want to remove: "))

    while number < 1 or number > len(to_do_list):
        number = int(input("Enter the task number which you want to remove: "))

    del to_do_list[number -1]
    print("The item was deleted")
    save_to_file(to_do_list) # save that after add
    return to_do_list



# Save the list to file
def save_to_file(to_do_list):
    outfile = open(FILE_NAME, "w")
    for task in to_do_list:
        outfile.write (f"{task}\n")
    
    # Close file
    outfile.close()

# Load from file 
def load_from_file():
    try:
        infile = open(FILE_NAME, "r")
        to_do_list = []

        for line in infile: # як тут закінчити? 
            
            to_do_list.append(line.strip())

        # Close file 
        infile.close()
        return to_do_list
    
    except:
        return []



# Call main function
main()
