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

def welcome_user():
    """
    Display welcome message 
    Ask the user to select an option
    """
    print("Welcome to Run Tracker!\n")
    print("With these training programmes you can learn to run 5-20 kilometers\nPick a training programme and track your progress!\n")

    while True:
        print("1) Select a new training plan")
        print("2) Input exercise data")
        print("3) View your progress\n")
        

        try:
            selected_option = int(input("What would you like to do? (select 1, 2, or 3): "))
            if selected_option not in [1, 2, 3]:
                raise ValueError (f"Select an option by typing either 1, 2 or 3. You typed {selected_option}")
        except ValueError as e:
            print(f"Invalid option: {e}, please try again\n")
            continue

        break

    if selected_option == 1:
        select_plan()
    # elif selected_option == 2:
    #     input_data()
    # elif selected_option == 3:
    #     view_progress()

        
def select_plan():
    """
    Get more information about the user's goals and propose a plan
    Raise a ValueError if invalid distance is given
    """
    user_names = SHEET.worksheet("user_plans").col_values(1)

    while True:
        try:
            user_name = input("Please select a user name: ")
            if user_name in user_names:
                raise RuntimeError (f"Username {user_name} already in use. Please select another username")
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

            while True:
                quit = input("Type q to quit this programme: ")    
                try:
                    if quit != "q":
                        raise ValueError (f"Expected the letter q. You typed {quit}")
                except ValueError as e:
                    print(f"Invalid data: {e}, please try again.")
                    continue
                else:
                    if quit == "q":
                        welcome_user()

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

    elif max_distance <= 15 and goal == 20:
        plan_number = 4
        
    print(f"We recommend you plan {plan_number}.\n")
    running_record = SHEET.worksheet("user_plans")
    running_record.append_row([user_name, plan_number])

    display_plan(plan_number)

def display_plan(plan_number):
    plans = SHEET.worksheet("plans")
    plan_data = plans.col_values(plan_number)
    
    header = ["Week", "Day 1", "Day 2", "Day 3"]

    data = [
        ["Week 1", plan_data[1], plan_data[2], plan_data[3]],
        ["Week 2", plan_data[4], plan_data[5], plan_data[6]],
        ["Week 3", plan_data[7], plan_data[8], plan_data[9]],
        ["Week 4", plan_data[10], plan_data[11], plan_data[12]],
        ["Week 5", plan_data[13], plan_data[14], plan_data[15]],
        ["Week 6", plan_data[16], plan_data[17], plan_data[18]],
        ["Week 7", plan_data[19], plan_data[20], plan_data[21]],
        ["Week 8", plan_data[22], plan_data[23], plan_data[24]]
    ]

    training_plan = tabulate(data, headers=header, tablefmt="grid")
    print("We recommend that you run three days a week ensuring that you leave at least one rest day inbetween each run.\nFor example you would run every Monday, Wednesday and Saturday.")
    print("Here is your training plan:\n")
    print(training_plan)
    print("\nPlease return next week to input that week's results.")




welcome_user()