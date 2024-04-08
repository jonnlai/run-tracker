# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# How to connect Google Sheets API to Python taken from Code Institute's Love Sandwiches project
import gspread
from google.oauth2.service_account import Credentials

# How to create a table taken from Geeks for geeks: https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('run-tracker')

RESULTS = SHEET.worksheet("results")
PLANS = SHEET.worksheet("plans")
SELECTED_PLANS = SHEET.worksheet("user_plans")
USER_NAMES = SHEET.worksheet("user_plans").col_values(1)

def welcome_user():
    """
    Display welcome message 
    Ask the user to select an option
    """
    print("\nWelcome to Run Tracker!\n")
    print("With these training programmes you can learn to run 5, 10, 15 or 20 kilometers.\nPick a training programme and track your progress!\n")

    while True:
        print("1) Select a new training plan")
        print("2) Input exercise data")
        print("3) View your progress and plan\n")
        
        try:
            selected_option = int(input("What would you like to do? (select 1, 2, or 3): "))
            if selected_option not in [1, 2, 3]:
                raise ValueError (f"Select an option by typing either 1, 2 or 3. You typed {selected_option}")
        except ValueError as e:
            print(f"Invalid option: {e}, please try again\n")
            continue

        break

    return selected_option

def return_to_start():
    """
    Function to allow the user to return to the start page
    """
    while True:
        quit = input("Type 'q' to quit this programme: ").lower()
        try:
            if quit != "q":
                raise ValueError (f"Expected the letter 'q'. You typed {quit}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            continue
        else:
            if quit == "q":
                main()

def select_plan():
    """
    Get more information about the user's goals and propose a plan
    Raise a ValueError if invalid distance is given
    """
    print("Please select a username that is 3-20 characters long and in lower case.")
    while True:
        try:
            user_name = input("Please select a user name: ").strip().lower()
            if user_name in USER_NAMES:
                raise RuntimeError (f"Username {user_name} already in use. Please select another username")
            if len(user_name) < 3 or len(user_name) > 20:
                raise RuntimeError (f"Username needs to be 3-15 characters long. You typed {user_name} which is {len(user_name)} characters long.") 
        except RuntimeError as e:
            print(f"Invalid data: {e}")
            continue
        break

    print(f"\nWelcome {user_name}! Please tell us a bit more about you and your goals.")
    
    while True:
        try:
            max_distance = int(input("What is the maximum distance in kilometers that you can run comfortably without stopping? (0 - 15) "))
            if max_distance < 0:
                raise ValueError (f"Number between 0 and 15 is required, you typed {max_distance}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            continue
        
        if max_distance > 15:
            print("You are already a very strong runner! Congratulations!\nThis programme is designed for people who can run less than 15 kilometers.\nWe recommend that you join a more advanced running programme.")
            return_to_start()

        break
        
    while True:        
        try:
            goal = int(input("What distance (in kilometers) would you like to be able to run: 5, 10, 15 or 20? "))
            if goal not in [5, 10, 15, 20]:
                raise ValueError (f"Select one of the following distances: 5, 10, 15 or 20. You typed {goal}")            
            if goal <= max_distance:
                raise ValueError (f"Set a goal that is higher than your current maximum distance ({max_distance}), you typed {goal}")
            if goal > max_distance + 10:
                raise ValueError (f"You are being ambitious! You cannot set a goal that is 10k higher than your current maximum distance ({max_distance}), you typed {goal}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            continue
        
        break

    # If the user inputs less than 5k as their current max, the programme won't allow them to choose a distance longer than 10k
    # If the user inputs 5-9k, the programme allows them to choose 10k or 15k distance
    # If ther user inputs 10-15k as their current max distance, the programme allows them to choose 15k or 20k
    if max_distance < 5 and goal == 5:
        plan_number = 1
    elif max_distance < 10 and goal == 10:
        plan_number = 2
    elif max_distance < 15 and goal == 15:
        plan_number = 3
    else:
        plan_number = 4
        
    print(f"We recommend you plan {plan_number}.\n")
    SELECTED_PLANS.append_row([user_name, plan_number]) # Add username and plan number to the selected plans worksheet
    RESULTS.append_row([user_name]) # Add username to the results worksheet

    return plan_number

def display_plan(plan_number):
    """
    Displays the training plan in a tablet format
    """
    plan_data = PLANS.row_values(plan_number)
    
    header = ["Week", "Day 1", "Day 2", "Day 3"]

    data = []

    week = 1
    activity = 1
    while week <= 8:
        data.append([f"Week {week}", plan_data[activity], plan_data[activity+1], plan_data[activity+2]])
        week += 1
        activity += 3

    training_plan = tabulate(data, headers=header, tablefmt="grid")

    print("We recommend that you run three days a week ensuring that you leave at least one rest day inbetween each run.\nFor example you would run every Monday, Wednesday and Saturday.\n")
    print("Here is your training plan:\n")
    print(training_plan)
    print("\nPlease return once a week to input that week's results.\n")

def check_username():
    """
    Ask the user to input their username and check whether it has been registered before
    """
    while True: 
        try:
            user_name = input("Please enter your registered username or type 'q' to quit: ").lower()
            # Check that the username given is a registred username
            if user_name not in USER_NAMES and user_name != "q":
                raise ValueError (f"{user_name} is not a registered username")
        except ValueError as e:
            print(f"Invalid choice: {e}, please try again or type 'q' to quit")
            continue
        else: 
            if user_name == "q":
                main()
            return user_name 

def check_week(user_name):
    """
    Check how many weeks of programme the user has completed.
    End the programme if they have completed 8 weeks already
    """
    user_row = RESULTS.find(user_name).row # Get the row number of the user record
    no_of_weeks = int((len(RESULTS.row_values(user_row))-1) / 3) # Divide the number of results by three to get the number of weeks (3 runs per week, remove the cell that contains username)

    if no_of_weeks == 8:
        print(f"Well done, {user_name}! You have completed the programme!")
        return_to_start()
    # else:
    #     return no_of_weeks

def input_data(user_name):
    """
    Allow user to input their last week's i.e. last three days' training data.
    Check that they have a registered username and that are inputting 3 integers as their training data values
    """
    check_week(user_name)
    print(f"\nWelcome back, {user_name}! Hope you enjoyed running last week!")
    # Validate the running date the user gives
    # How to validate the data the user inputs taken from Code Institute's Love Sandwiches project
    while True:
        print("\nPlease enter your running data from last week i.e. your last three runs.")
        print("You should type three numbers, separated by commas.\nIf you missed a run, you should indicate that by typing 0.")
        print("For example: 3,0,2\n")

        runs_input = input("Please enter your running data here: \n")
        running_data = runs_input.split(",")

        try:
            [int(run) for run in running_data]
            if len(running_data) != 3:
                raise ValueError (f"Three values required, you provided {len(running_data)}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            continue
        else:
            try:
                check_input = input(f"You typed: {running_data}. Are these correct? (y/n) ").lower() # Ask the user to confirm the data
                if check_input != "y" and check_input != "n":
                    raise ValueError (f"Type 'y' to confirm the data is correct or 'n' to re-type the data")
            except ValueError as e:
                print(f"Invalid selection: {e}, please try again.")
                continue
            else:
                if check_input == "y":
                    user_row = RESULTS.find(user_name).row # Get the row number of the user record
                    
                    # Add the running data the user has inputted in the results worksheet
                    for data in running_data:
                        next_result = len(RESULTS.row_values(user_row))+1 # Get the number of values recorded and add one to indicate where the next result is added
                        RESULTS.update_cell(user_row, next_result, data) # Add the inputted data into the next empty cell using row and column coordinates
                elif check_input == "n":
                    continue
        break

    print("\nThank you for adding your latest running results!")
    print("Keep on running and don't forget to come back next week to add your results!\n")

def display_next_week(user_name):
    """
    Display next week's training plan to the user
    """
    check_week(user_name)
    user_row = SELECTED_PLANS.find(user_name).row # Get the row number of the user record
    plan_number = SELECTED_PLANS.row_values(user_row)[1] # Get the number of the user's plan. All plan numbers are stored in column 2

    next_activity = int((len(RESULTS.row_values(user_row)))) # Get the number of activities recorded by the user + 1
    next_week = PLANS.row_values(plan_number)[next_activity:next_activity+3] # Get the next three activities from the list

    header = ["Week", "Day 1", "Day 2", "Day 3"]

    data = []

    data.append([f"Week {int((next_activity-1)/3+1)}", next_week[0], next_week[1], next_week[2]])

    next_week_plan = tabulate(data, headers=header, tablefmt="grid")
    
    print(f"\nYou have been following this 8 week programme for {int((next_activity-1)/3)} week(s).")
    print("Here is your next week's plan:\n")
    print(next_week_plan)

def view_progress(user_name):
    """
    Display a table that shows all the data the user has recorded
    """
    user_row = RESULTS.find(user_name).row # Get the row number of the user record
    user_data = RESULTS.row_values(user_row)
    no_of_weeks = int((len(RESULTS.row_values(user_row))-1) / 3) # Divide the number of results by three to get the number of weeks (3 runs per week, remove the cell that contains username)
    user_row = SELECTED_PLANS.find(user_name).row # Get the row number of the user record
    plan_number = SELECTED_PLANS.row_values(user_row)[1] # Get the number of the user's plan. All plan numbers are stored in column 2

    print(f"\nYou have been following this 8 week programme for {no_of_weeks} week(s).")
    print("Here are your results so far:\n")
    
    header = ["Week", "Day 1", "Day 2", "Day 3"]

    data = []

    # Create a list of lists of each week's results
    week = 1
    activity = 1
    while week <= no_of_weeks:
        data.append([f"Week {week}", user_data[activity], user_data[activity+1], user_data[activity+2]])
        week += 1
        activity += 3

    user_results = tabulate(data, headers=header, tablefmt="grid")
    print(user_results)

    while True:
        try:
            view_plan = input("Would you like to view your plan? (y/n) ").lower()
            if view_plan != "y" and view_plan != "n":
                raise ValueError (f"Expected the letter 'y' or 'n'. You entered {view_plan}")
        except ValueError as e:
            print(f"Invalid option: {e}, please try again.")
            continue
        else:
            if view_plan =="y":
                display_plan(plan_number)
            else:
                break

def main():
    """
    Function to run all the other functions
    """
    selected_option = welcome_user()
    
    if selected_option == 1:
        plan_number = select_plan()
        display_plan(plan_number)
    elif selected_option == 2:
        user_name = check_username()
        check_week(user_name)
        input_data(user_name)            
        display_next_week(user_name)
    elif selected_option == 3:
        user_name = check_username()
        view_progress(user_name)
        
    return_to_start()

main()