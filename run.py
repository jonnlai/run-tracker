"""
How to create a table taken from Geeks for geeks:
https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
"""
from tabulate import tabulate

"""
How to connect Google Sheets API to Python taken from
 Code Institute's Love Sandwiches project
"""
import gspread
from google.oauth2.service_account import Credentials

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
    print("""
                  88bd88b?88   d8P  88bd88b
                  88P'  `d88   88   88P' ?8b
                 d88     ?8(  d88  d88   88P
                d88'     `?88P'?8bd88'   88b

                                   d8b
   d8P                             ?88
d888888P                            88b
  ?88'    88bd88b d888b8b   d8888b  888  d88' d8888b  88bd88b
  88P     88P'  `d8P' ?88  d8P' `P  888bd8P' d8b_,dP  88P'  `
  88b    d88     88b  ,88b 88b     d88888b   88b     d88
  `?8b  d88'     `?88P'`88b`?888P'd88' `?88b,`?888P'd88'
    """)

    print("Welcome to Run Tracker!\n")
    print("Learn to run 5, 10, 15 or 20 kilometers"
          " with these 8-week training programmes.\n"
          "Pick a training programme and track your progress!\n")

    while True:
        print("1) Select a new training plan")
        print("2) Input exercise data")
        print("3) View your progress and plan\n")

        try:
            selected_option = int(input("What would you like to do?"
                                        " (select 1, 2, or 3): \n"))
            if selected_option not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print(f"Invalid option. Expected 1, 2 or 3. Please try again.\n")
            continue

        break

    return selected_option


def return_to_start():
    """
    Function to allow the user to return to the start page
    """
    while True:
        quit = input("Type 'q' to return to the main page: \n").lower()
        try:
            if quit != "q":
                raise ValueError(f"Expected the letter 'q'. You typed {quit}")
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
    print("\nPlease select a username that is 3-20 characters long"
          " and in lower case.")

    while True:
        try:
            username = input("Please select a username or type 'q'"
                             " to quit: \n").strip().lower()
            if username in USER_NAMES and username != "q":
                raise RuntimeError(f"Username {username} already in use."
                                   " Please select another username")
            if (len(username) < 3 or len(username) > 20) and username != "q":
                raise RuntimeError("Username needs to be 3-15 characters "
                                   f"long.\n You typed {username} which is"
                                   f" {len(username)} characters long.")
        except RuntimeError as e:
            print(f"Invalid choice: {e}")
            continue
        else:
            if username == "q":
                main()
        break

    print(f"\nWelcome {username}!"
          " Please tell us a bit more about you and your goals.")

    """
    Ask user for their current maximum distance
    If the distance is longer than 15k,
    the user is advised to seek a more advanged programme
    """
    while True:
        try:
            max_distance = int(input("What's the maximum distance in "
                                     "kilometers that you can run "
                                     "without stopping? (0 - 15) \n"))
            if max_distance < 0:
                raise ValueError
        except ValueError:
            print(f"A whole number between 0 and 15 is required, "
                  "please try again.\n")
            continue
        else:
            if max_distance > 15:
                print("\nYou are already a very strong runner!"
                      "Congratulations!\nThis programme is designed for people"
                      " who can run less than 15 kilometers.\nWe recommend"
                      " that you join a more advanced running programme.\n")
                return_to_start()

        break
    
    """
    Ask user to set a goal
    The goal needs to be higher than max distance but cannot be
    more than 10k longer than their current maximum distance
    """
    while True:
        goal = input("What distance (in kilometers) would you"
                     " like to be able to run: 5, 10, 15 or 20? \n")
        try:
            if goal.isdigit() is False:
                raise ValueError(f"Expected a number. You typed {goal}")
            if int(goal) not in [5, 10, 15, 20]:
                raise ValueError("Select one of the following distances:"
                                 f" 5, 10, 15 or 20. You typed {goal}")
            if int(goal) <= max_distance:
                raise ValueError("Set a goal that is higher than your" 
                                 f"current maximum distance ({max_distance})"
                                 f", you typed {goal}")
            if int(goal) > max_distance + 10:
                raise ValueError("You are being ambitious! You cannot set"
                                 " a goal that is 10k higher than your "
                                 f"current maximum distance ({max_distance})."
                                 f" You typed {goal}")
        except ValueError as e:
            print(f"Invalid choice: {e}, please try again.\n")
            continue
        else:
            goal = int(goal)
        
        break

    """
    If the user inputs less than 5k as their current max,
    the programme won't allow them to choose a distance longer than 10k.
    If the user inputs 5-9k, the programme allows them to choose 10k or 15k
    If ther user inputs 10-15k as their current max distance,
    the programme allows them to choose 15k or 20k
    """
    if max_distance < 5 and goal == 5:
        plan_number = 1
    elif max_distance < 10 and goal == 10:
        plan_number = 2
    elif max_distance < 15 and goal == 15:
        plan_number = 3
    elif max_distance <= 15 and goal == 20:
        plan_number = 4

    """
    Add username and plan number to the selected_plans worksheet
    Add username to the results worksheet
    """  
    print(f"We recommend you plan {plan_number}.\n")
    SELECTED_PLANS.append_row([username, plan_number])
    RESULTS.append_row([username])

    return plan_number


def display_plan(plan_number):
    """
    Displays the training plan in a tablet format
    Give the user instructions how to plan their week
    and when to input their data
    """
    plan_data = PLANS.row_values(plan_number)

    header = ["Week", "Day 1", "Day 2", "Day 3"]

    data = []

    week = 1
    activity = 1
    while week <= 8:
        data.append([f"Week {week}", plan_data[activity] + " km",
                     plan_data[activity+1] + " km",
                     plan_data[activity+2] + " km"])
        week += 1
        activity += 3

    training_plan = tabulate(data, headers=header, tablefmt="grid")

    print("We recommend that you run three days a week ensuring that you "
          "leave at least one rest day inbetween each run.\n"
          "For example you would run every Monday, Wednesday and Saturday.\n")
    print("Here is your training plan:\n")
    print(training_plan)
    print("\nPlease return once a week to input that week's results.\n")


def check_username():
    """
    Ask the user to input their username and
    check whether it has been registered before
    """
    while True: 
        try:
            username = input("Please enter your registered username"
                             " or type 'q' to quit: \n").lower()
            # Check that the username given is a registred username
            if username not in USER_NAMES and username != "q":
                raise ValueError(f"{username} is not a registered username")
        except ValueError as e:
            print(f"Invalid choice: {e}, please try again or type 'q' to quit")
            continue
        else:
            if username == "q":
                main()
            return username


def check_week(username):
    """
    Check how many weeks of programme the user has completed.
    End the programme if they have completed 8 weeks already
    """
    # Get the row number of the user record
    user_row = RESULTS.find(username).row
    # Divide the number of results(-1) by three to get the number of weeks
    no_of_weeks = int((len(RESULTS.row_values(user_row))-1) / 3)

    if no_of_weeks == 8:
        print(f"Well done, {username}! You have completed the programme!")
        return_to_start()


def input_data(username):
    """
    Allow user to input their last week's i.e. last three days' training data.
    Check that they have a registered username and
    that they are inputting 3 integers as their training data values
    """
    check_week(username)
    print(f"\nWelcome back, {username}! Hope you enjoyed running last week!")
    # Validate the running date the user gives
    # How to validate the data taken from CI's Love Sandwiches project
    while True:
        print("\nPlease enter your running data from last week"
              " (your last three runs).")
        print("You should enter three numbers, separated by commas.\n"
              "If you missed a run, you should indicate that by typing 0.")
        print("For example: 3,0,2\n")

        runs_input = input("Please enter your running data here: \n")
        running_data = runs_input.split(",")

        try:
            [int(run) for run in running_data]
            if len(running_data) != 3:
                raise ValueError(f"Three values required,"
                                 f" you provided {len(running_data)}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            continue
        else:
            try:
                check_input = input(f"You typed: {running_data}. "
                                    "Are these correct? (y/n) \n").lower()
                if check_input != "y" and check_input != "n":
                    raise ValueError(f"Type 'y' to confirm the data is correct"
                                     " or 'n' to re-enter the data")
            except ValueError as e:
                print(f"Invalid selection: {e}, please try again.")
                continue
            else:
                if check_input == "y":
                    # Get the row number of user record
                    user_row = RESULTS.find(username).row
                    # Add the running data inputted into the results worksheet
                    for data in running_data:
                        # number of values recorded plus 1
                        next_result = len(RESULTS.row_values(user_row))+1
                        # Add into the next empty cell using row and col coords
                        RESULTS.update_cell(user_row, next_result, data)
                elif check_input == "n":
                    continue
        break

    print("\nThank you for adding your latest running results!")
    print("Keep on running and don't forget to come back next week"
          " to add your results!\n")


def display_next_week(username):
    """
    Display next week's training plan to the user
    """
    check_week(username)
    # Get the row number of the user record
    user_row = SELECTED_PLANS.find(username).row
    # Get the number of user's plan. All plan numbers are stored in column 2
    plan_number = SELECTED_PLANS.row_values(user_row)[1]
    # Get the number of activities recorded by the user + 1
    next_activity = int((len(RESULTS.row_values(user_row))))
    # Get the next three activities from the list
    next_week = PLANS.row_values(plan_number)[next_activity:next_activity+3]

    header = ["Week", "Day 1", "Day 2", "Day 3"]

    data = []

    data.append([f"Week {int((next_activity-1)/3+1)}", 
                 next_week[0], next_week[1], next_week[2]])

    next_week_plan = tabulate(data, headers=header, tablefmt="grid")

    print(f"\nYou have been following this 8 week programme for"
          f"{int((next_activity-1)/3)} week(s).")
    print("Here is your next week's plan:\n")
    print(next_week_plan)


def view_progress(username):
    """
    Display a table that shows all the data the user has recorded
    Get the row number of the user record
    Divide the number of results minus 1 by three to get the number of weeks
    """
    user_row = RESULTS.find(username).row
    user_data = RESULTS.row_values(user_row)
    no_of_weeks = int((len(RESULTS.row_values(user_row))-1) / 3)
    user_row = SELECTED_PLANS.find(username).row
    plan_number = SELECTED_PLANS.row_values(user_row)[1]

    print("\nYou have been following this 8 week programme"
          f" for {no_of_weeks} week(s).")
    print("Here are your results so far:\n")

    header = ["Week", "Day 1", "Day 2", "Day 3"]

    data = []

    # Create a list of lists of each week's results
    week = 1
    activity = 1
    while week <= no_of_weeks:
        data.append([f"Week {week}", user_data[activity],
                     user_data[activity+1], user_data[activity+2]])
        week += 1
        activity += 3

    user_results = tabulate(data, headers=header, tablefmt="grid")
    print(user_results)

    while True:
        try:
            view_plan = input("Would you like to view"
                              " your plan? (y/n) \n").lower()
            if view_plan != "y" and view_plan != "n":
                raise ValueError(f"Expected the letter 'y' or 'n'."
                                 f" You entered {view_plan}")
        except ValueError as e:
            print(f"Invalid option: {e}, please try again.")
            continue
        else:
            if view_plan == "y":
                display_plan(plan_number)
                break
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
        username = check_username()
        check_week(username)
        input_data(username)
        display_next_week(username)
    elif selected_option == 3:
        username = check_username()
        view_progress(username)

    return_to_start()


main()
