from task_functions import *
the_menu = {"L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"}


all_tasks = [
    {
    },
    {
     
    },
    {
     
    }

]

list_menu = {
    "A": "all tasks",
    "C": "completed tasks",
    "I": "incomplete tasks"
}

priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}


opt = None

while True:
    print_main_menu(the_menu) # TODO 2: define the function, uncomment, and call with the menu as an argument
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters

    if opt not in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == "Q": # TODO 4: quit the program
        print("Goodbye!\n")
        break # exit the main `while` loop
        
    elif opt == 'L':
        if all_tasks == []:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue
        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_tasks(all_tasks, priority_scale)
            input("::: Press Enter to continue")
        elif subopt == 'C':
            print_tasks(all_tasks, priority_scale, completed = 'yes')
            input("::: Press Enter to continue")
        elif subopt == 'I':
            print_tasks(all_tasks, priority_scale, completed = 'no')
            input("::: Press Enter to continue")
            
    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter each required field, separated by commas.")
            print("::: name, info, priority, MM/DD/YYYY, is task done? (yes/no)")
            in_list = input("> ") # TODO: get and process the data into a list
            in_list = in_list.split(",")
            result = get_new_task(in_list, priority_scale) # TODO: attempt to create a new task
            if type(result) == dict:
                all_tasks.append(result) # TODO: add a new task to the list of tasks
                print(f"Successfully added a new task!")
                print_task(result, priority_scale, name_only = False)
            elif type(result) == int:
                print(f"WARNING: invalid number of fields!")
                print(f"You provided {result}, instead of the expected 5.\n")
            else:
                print(f"WARNING: invalid task field: {result}\n")

            print("::: Would you like to add another task?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
            # ----------------------------------------------------------------
            
    elif opt == 'U':
        continue_action = 'y'
        while continue_action == 'y':
            if all_tasks == []: # TODO
                print("WARNING: There is nothing to update!")
                break
            print("::: Which task would you like to update?")
            print_tasks(all_tasks, priority_scale, name_only = True, show_idx = True, start_idx = 1)
            print("::: Enter the number corresponding to the task.")
            user_option = input("> ")
            if is_valid_index(user_option, all_tasks) == True: # TODO
                # TODO: convert the index appropriately to account for the start_idx = 1
                subopt = get_selection("update", all_tasks[int(user_option)-1], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") # TODO
                field_info = input("> ")
                result = update_task(all_tasks, user_option, priority_scale, subopt, field_info, start_idx = 1)
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  # TODO
                    print_task(result, priority_scale)  # TODO
                else: # update_task() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  # TODO
                    print(f"The task was not updated.")
            else: # is_valid_index() returned False
                print(f"WARNING: |{user_option}| is an invalid task number!")  # TODO

            print("::: Would you like to update another task?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
        input("::: Press Enter to continue")
            # ----------------------------------------------------------------
    elif opt == 'D':
        continue_action = 'y'
        while continue_action == 'y':
            print("Which task would you like to delete?")
            print("A - Delete all tasks at once")
            print_tasks(all_tasks, priority_scale, show_idx=True, name_only = True)
            print("::: Enter the number corresponding to the task")
            print("::: or press 'M' to return to the main menu.")
            user_option = input("> ")
            if user_option == "A":
                print("::: WARNING! Are you sure you want to delete All tasks?")
                print("::: Type Yes to continue the deletion.")
                user_opt = input("> ")
                if user_opt == "Yes":
                    all_tasks = []
                    print("Deleted all tasks.")
                    continue_action = 'n'
                    break
            result = delete_item(all_tasks, user_option, start_idx=1)
            if type(result) == dict:
                print("Success!")
                print("Deleted the task", "|"+result["name"]+"|")
            elif result == 0:
                print("WARNING: there is nothing to delete!")
            elif result == -1:
                print(f"WARNING: |{user_option}| is an invalid task number!")
            print("::: Would you like to delete another task?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()
        input("::: Press Enter to continue")
    
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            value = save_tasks_to_csv(all_tasks, filename) # TODO: Call the function with appropriate inputs and capture the output
            if value == -1: # TODO
                print(f"WARNING: |{filename}| is an invalid file name!") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all tasks to |{filename}|")
                continue_action = 'n'
                input("::: Press Enter to continue")

            
    
    elif opt == 'R':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            value = load_tasks_from_csv(filename, all_tasks, priority_scale)
            if value == None:
                print(f"WARNING: |{filename}| was not found!")
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            elif value == -1:
                print(f"WARNING: |{filename}| is an invalid file name!")
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(value)
                print(f"Successfully retreived data from |{filename}|")
                print("::: Would you like to retreive another task?", end=" ")
                continue_action = input("Enter 'y' to continue.\n> ")
                continue_action = continue_action.lower()
        input("::: Press Enter to continue")
    
print("Have a nice day!")
