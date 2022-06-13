
def print_main_menu(menu):
    """
    prints the main menu
    """
    print("="*26)
    print("What would you like to do?")
    for key, value in menu.items():
        print(key, "-", value)
    print("="*26)
def get_written_date(date_str):
    """
    The function turns a date in string format into a printed date
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    date = ""
    # Finish the function
    if type(date_str) == str:
        
        date = f'{month_names[int(date_str[0:2])]} {int(date_str[3:5])}, {date_str[6:10]}'
    elif type(date_str) == list:
        date = f'{month_names[int(date_str[0])]} {int(date_str[1])}, {date_str[2]}'
    # Return the date string in written format
    return date

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection].lower()}|.")
    return selection


def print_task(task, priority_map, name_only = False):
    """
    param: task (dict) - a dictionary object that is expected
            to have the following string keys:
    - "name": a string with the task's name
    - "info": a string with the task's details/description
            (the field is not displayed if the value is empty)
    - "priority": an integer, representing the task's priority
        (defined by a dictionary priority_map)
    - "duedate": a valid date-string in the US date format: <MM>/<DD>/<YEAR>
            (displayed as a written-out date)
    - "done": a string representing whether a task is completed or not

    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed for the
            priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.

    returns: None; only prints the task values

    Helper functions:
    - get_written_date() to display the 'duedate' field
    """
    if name_only == True:
        print(task["name"])
    else:
        print(task["name"])
        if task["info"] != "":
            print("  *", task["info"])
        print("  * Due:", get_written_date(task["duedate"]), " (Priority:", priority_map[task["priority"]] + ")")
        print("  * Completed?", task["done"])
def print_tasks(task_list, priority_map, name_only = False,
                show_idx = False, start_idx = 0, completed = "all"):
    """
    param: task_list (list) - a list containing dictionaries with
            the task data
    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed 
            for the priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.
            Passed as an argument into the helper function.
    param: show_idx (Boolean) - by default, set to False.
            If False, then the index of the task is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            task name.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets displayed for the first task, if show_idx is True.
    param: completed (str) - by default, set to "all".
            By default, prints all tasks, regardless of their
            completion status ("done" field status).
            Otherwise, it is set to one of the possible task's "done"
            field's values in order to display only the tasks with
            that completion status.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-"*42)
    idx = start_idx+1
    for task in task_list: # go through all tasks in the list
        if show_idx: # if the index of the task needs to be displayed
            print(f"{idx - start_idx}.", end=" ")
        if completed == "all":
            print_task(task, priority_map, name_only)
        elif completed == "yes":
            if (task["done"] == "yes"):
                print_task(task, priority_map, name_only)
        else:
            if (task["done"] == "no"):
                print_task(task, priority_map, name_only)
        idx += 1


def is_valid_index(idx, in_list, start_idx = 0):
    """
    checks to see if a list can be indexed at a certain index
    """
    if type(idx) == str and idx.isdigit() == True:
        if int(idx) - start_idx >= 0 and int(idx)-start_idx < len(in_list):
            return True
        else:
            return False
    else:
        return False


def delete_item(in_list, idx, start_idx = 0):
    """
    param: in_list - a list from which to remove an item
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of an item in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from in_list.

    returns:
    If the input list is empty, return 0.
    If idx is not of type string or start_idx is not an int, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.

    Helper functions:
    - is_valid_index()
    """
    if in_list == []:
        return 0
    elif type(idx) != str or type(start_idx) != int:
        return None
    elif is_valid_index(idx, in_list, start_idx) == False:
        return -1
    else:
        return in_list.pop((int(idx)-start_idx))

def is_valid_name(string):
    """
    

    Parameters
    ----------
    string : input string

    Returns
    -------
    bool
        true if string is a valid name, false is string is invalid

    """
    if type(string) == str:
        if 3 <= len(string) <= 25:
            return True
        else:
            return False
    else:
        return False
    
def is_valid_priority(string, dictionary):
    """
    


    ----------
    checks if a given string is in the dictionary, returns a bool
    """
    if type(string) == str and type(dictionary) == dict:
        if str.isdigit(string) == True:
            if int(string) in dictionary.keys():
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_date(string):
    """
    

    Parameters
    ----------
    returns a booll based on if string is a valid date
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if type(string) == str and string[0:2].isdigit() == True and string[2] == "/" and string[5] == "/":
        if 1 <= int(string[0:2])<= 12:
            if 1 <= int(string[3:5]) <= num_days[int(string[0:2])]:
                if int(string[6:]) >= 1000:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_completion(string):
    """
    checks if given string is either 'yes' or 'no'
    returns true if true, false if false
    

    """
    if string == "yes" or string == "no":
        return True
    else:
        return False

def get_new_task(in_list, priority_scale):
    """
    takes in a given list and the priority scale dictionary
    checks if the list is of length 5 and if every element in the list is a string
    if yes, checks if the strings are valid names, prio, dates, and done
    returns the tuple of the wrong string in the form (type, string) if it doesn't pass tests'
    """
    in_dict = {
    "name": ...,
    "info": ...,
    "priority": ...,
    "duedate": ...,
    "done": ...
    }
    if len(in_list) != 5:
        return len(in_list)
    for element in in_list:
        if type(element) != str:
            return("type" , element)

    if is_valid_name(in_list[0]) == True and is_valid_priority(in_list[2], priority_scale) == True and is_valid_date(in_list[3]) == True and is_valid_completion(in_list[4]) == True:
        in_dict = {"name" : in_list[0],
                   "info" : in_list[1],
                   "priority": int(in_list[2]),
                   "duedate" : in_list[3],
                   "done": in_list[4]}
        return in_dict
    else:
        if is_valid_name(in_list[0]) == False:
            return ("name", in_list[0])
        elif is_valid_priority(in_list[2], priority_scale) == False:
            return ("priority", in_list[2].strip())
        elif is_valid_date(in_list[3]) == False:
            return ("duedate", in_list[3].strip())
        elif is_valid_completion(in_list[4]) == False:
            return ("done", in_list[4].strip())
        

    
def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
    """
    param: info_list - a list that contains task dictionaries
    param: idx (str) - a string that is expected to contain an integer
            index of an item in the input list
    param: start_idx (int) - by default is set to 0;
            an expected starting value for idx that gets subtracted
            from idx for 0-based indexing
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.

    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.

    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
    Depending on the field_key, it also calls:
    - is_valid_name()
    - is_valid_priority()
    - is_valid_date()
    - is_valid_completion()
    """
    if info_list == []:
        return 0
    elif is_valid_index(idx, info_list, start_idx) == False:
        return -1
    elif field_key not in info_list[int(idx)-start_idx].keys():
        return -2
    
    
    elif is_valid_name(info_list[int(idx)-start_idx][field_key]) == True and field_key == "name":
        info_list[int(idx)-start_idx][field_key] = field_info
        return info_list[int(idx)-start_idx]
    
    elif field_key == "info":
        info_list[int(idx)-start_idx][field_key] = field_info
        return info_list[int(idx)-start_idx]
    
    elif is_valid_priority(info_list[int(idx)-start_idx][field_key], priority_map) == True and field_key == "priority":
        info_list[int(idx)-start_idx][field_key] = field_info
        return info_list[int(idx)-start_idx]
    
    elif is_valid_date(info_list[int(idx)-start_idx][field_key]) == True and field_key == "duedate":
        info_list[int(idx)-start_idx][field_key] = field_info
        return info_list[int(idx)-start_idx]
    
    elif is_valid_completion(info_list[int(idx)-start_idx][field_key]) == True and field_key == "done":
        info_list[int(idx)-start_idx][field_key] = field_info
        return info_list[int(idx)-start_idx]
    
    else:
        return field_key
def load_tasks_from_csv(filename, in_list, priority_map):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_list (list) - A list of task dictionary objects to which
            the tasks read from the provided filename are appended.
            If in_list is not empty, the existing tasks are not dropped.
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed by the helper function.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new task using the `get_new_task()` function.
    - If the function `get_new_task()` returns a valid task object,
    it gets appended to the end of the `in_list`.
    - If the `get_new_task()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid task data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_task().

    Helper functions:
    - get_new_task()
    """
    import csv
    import os
    dtask = []
    counter = 0
    if filename[-4:] != ".csv":
        return -1
    elif os.path.exists(filename) == False:
        return None
    else:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for i in reader:
                x = get_new_task(i, priority_map)
                counter += 1
                if type(x) == dict:
                    in_list.append(x)
                else:
                    dtask.append(x)
    return in_list, dtask


def save_tasks_to_csv(tasks_list, filename):
    """
    param: tasks_list - The list of the tasks stored as dictionaries
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the tasks. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every task in the list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the list is:

    * `name` field of the task dictionary
    * `info` field of the task dictionary
    * `priority` field of the task as a string
    (i.e, "5" or "3", NOT "Lowest" or "Medium")
    * `duedate` field of the task as written as string
    (i.e, "06/06/2022", NOT "June 6, 2022")
    * `done` field of the task dictionary

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    if filename[-4:] != ".csv":
        return -1
    else:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for task in tasks_list:
                writer.writerow(task.values())
