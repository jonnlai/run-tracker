# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# How to connect Google Sheets API to Python taken from Code Institute's Love Sandwiches project
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

def welcome_user():
    """
    Display welcome message 
    Ask the user to select an option
    """
    print("Welcome to Run Tracker!\n")
    print("Pick a training programme and track your progress!\n")

    while True:
        print("1) Pick a new training plan")
        print("2) Input exercise data")
        print("3) View your progress\n")
        selected_option = input("What would you like to do? (select 1, 2, or 3): ")

        try:
            if int(selected_option) != 1 and int(selected_option) != 2 and int(selected_option) != 3:
                raise ValueError (f"Select an option by typing either 1, 2 or 3. You typed {selected_option}")
        except ValueError as e:
            print(f"Invalid option: {e}, please try again\n")
            continue

        break



welcome_user()