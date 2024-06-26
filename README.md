# Run Tracker

![Mockup image](readme-files/mockup-image.png)

Run Tracker helps users learn to run 5, 10, 15 or 20 kilometers in 8-weeks. The application recommends a training plan and allows the user to track and view their progress. The users are asked to return weekly to input that week's running data (i.e. their last three runs).

The deployed project can be found here: [Run Tracker](https://running-programme-694cea56c7e6.herokuapp.com/)

## Table of Content

1. [User Experience (UX)](#user-experience-ux)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)

## User Experience (UX)

### Project Goals

- Help users improve their fitness level by providing them with an easy way to start running or to increase the distance they can run.
- Allow users to track their progress for the duration of the programme.
- Validate the data the user inputs to ensure that the programme works correctly and provides a good user experience.

### User Stories

- As someone new to running, I want an easy-to-follow plan that gives me the weekly structure that I need in order to be able to start running.
- As a beginner or intermediate runner, I want a programme that helps me push my limits and get better results.
- As a user of the application, I want to be able to store my running data.
- As a user of the application, I want to be able to view my progress and compare that to my plan.

### Flowchart

A flowchart to plan the logic of the programme was created using [Lucid](https://lucid.app/).

![Flowchart](readme-files/flowchart.png)

### Data Model

The data that the user inputs is initially stored as variables. Once all the necessary data has been inputted by the user and validated, it is added to a Google Sheets.

Three worksheets are being used:

- one to store the four different running plans that the programme offers
- one to store which plan each user has chosen
- one to store the user's weekly running data

### Colour Scheme

[Colorama](https://pypi.org/project/colorama/) was used to add colour to the terminal to make the application more intuitive and easier to use.

The following colours were used:

- The ASCII art, the name of the application, and all text that contains information or guidance are displayed in green.
- Inputs and requests to input data are displayed in the default colour.
- Errors are displayed in red.
- The three menu options are all displayed in different colours: magenta, cyan, and yellow.

[Back to top](#run-tracker)

## Features

### Main page

The user is given information about the application and is asked to select an option.

![Main page](readme-files/mockup-image.png)

### Select plan

This function asks the user to select a username and collects information from the user in order to be able to select the most suitable plan for them based on the maximum distance that the user can currently run and their goal. The username and the user's selected plan are added to Google Sheets.

![Select plan](readme-files/features/select-plan.png)

### View plan

This function displays the selected 8-week plan to the user and advises them when to return to input their results.

![View plan](readme-files/features/view-plan.png)

### Input data

This function asks the user to input their username, and if the username is recognised, it allows the user to input their previous week's running data.

![Input data](readme-files/features/input-data.png)

### Next week's plan

After the user has added their latest running data, next week's plan is displayed to the user, and they are encouraged to keep following the running programme and to return the following week to add that week's results.

![Next week](readme-files/features/next-week.png)

### Programme finished

This informs the user that they have finished the programme and advises them how they can view their results.

![Programme finished](readme-files/features/programme-finished.png)

### View progress

This function asks the user to input their username, and if the username is recognised, it allows the user to view their results and their plan.

![View progress](readme-files/features/view-progress.png)

### Google Sheets

Three worksheets have been used to store data.

#### Plans

The application offers four different running plans that are stored in the "plans" worksheet. Each row holds the name of the plan and 24 numbers (3 runs per week for 8 weeks) that indicate the distances the user should run to achieve their goal in 8 weeks.

![Plans](readme-files/features/sheet-plans.png)

#### User Plans

The "user_plans" worksheet holds all the usernames and the number of the plan that each user is following.

![User plans](readme-files/features/sheet-user-plans.png)

#### Results

The "results" worksheet holds all the usernames and the runs that the users have recorded.

![Results](readme-files/features/sheet-results.png)

[Back to top](#run-tracker)

## Technologies Used

### Language Used

- [Python3](https://www.python.org/)

### Frameworks, Libraries, and Programmes Used

- [Lucid](https://lucid.app/) was used to create the programme flowchart.

- [VSCode](https://code.visualstudio.com/) was used for writing code, committing, and then pushing to GitHub.

- [GitHub](https://github.com/) was used to store the project after pushing.

- [Heroku](https://id.heroku.com/) was used to deploy the application.

- [CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code.

- [Tabulate](https://pypi.org/project/tabulate/) library was used to present the data in table format.

- [Colorama](https://pypi.org/project/colorama/) library was used to apply colour to the terminal text.

- [Google Sheets](https://docs.google.com/spreadsheets) was used to store the data.

- [Gspread](https://docs.gspread.org/en/v6.0.0/) library was used to read and write Google Sheets.

[Back to top](#run-tracker)

## Testing

### Testing User Stories

- As someone new to running, I want an easy-to-follow plan that gives me the weekly structure that I need in order to be able to start running.

  - The application gives the user a weekly plan that helps them structure their week.

- As a beginner or intermediate runner, I want a programme that helps me push my limits and get better results.

  - The application offers four different plans with different difficulty levels.

- As a user of the application, I want to be able to store my running data.

  - The application stores the data that the user inputs.
  - The application validates the data to ensure that the data inputted is correct.

- As a user of the application, I want to be able to view my progress and compare that to my plan.
  - The application allows the user to view their weekly progress.
  - The application allows the user to view their plan whenever they want so that they can compare that to their results.

### Code Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code for PEP8 requirements.

When the code was validated for the first time, the following warning and error messages were received:

![Python Linter 1](readme-files/python-linter/python-linter-1.png)
![Python Linter 2](readme-files/python-linter/python-linter-2.png)
![Python Linter 3](readme-files/python-linter/python-linter-3.png)
![Python Linter 4](readme-files/python-linter/python-linter-4.png)
![Python Linter 5](readme-files/python-linter/python-linter-5.png)
![Python Linter 6](readme-files/python-linter/python-linter-6.png)
![Python Linter 7](readme-files/python-linter/python-linter-7.png)
![Python Linter 8](readme-files/python-linter/python-linter-8.png)
![Python Linter 9](readme-files/python-linter/python-linter-9.png)

The warnings and errors were addressed, and it was confirmed that no errors remained. The code was validated again when the development had finished, confirming that it contained no errors.

![No errors](readme-files/python-linter/no-errors.png)

### Manual Testing

<table>
    <tr>
        <th>Feature</th>
        <th>Outcome</th>
        <th>Example</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=3>Select option</td>
        <td>Validate if value is empty</td>
        <td><img src=readme-files/testing/select-option-empty-test.png alt="Value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is an integer other than 1, 2 or 3</td>
        <td><img src=readme-files/testing/select-option-num-test.png alt="Value is an integer not 1,2,3"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not an integer</td>
        <td><img src=readme-files/testing/select-option-string-test.png alt="Value is a string"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=4>Select username</td>
        <td>Validate if value is empty</td>
        <td><img src=readme-files/testing/select-username-empty.png alt="Username is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is shorter than 3 characters</td>
        <td><img src=readme-files/testing/select-username-short.png alt="Username is shorter than 3 char"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is longer than 15 characters</td>
        <td><img src=readme-files/testing/select-username-long.png alt="Username is longer than 15 char"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is already in use</td>
        <td><img src=readme-files/testing/select-username-in-use.png alt="Username is already in use"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=3>Enter maximum distance</td>
        <td>Validate if value is empty</td>
        <td><img src=readme-files/testing/maximum-distance-empty.png alt="Max distance is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not an interger</td>
        <td><img src=readme-files/testing/maximum-distance-string.png alt="Max distance is not an interger"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is over 15</td>
        <td><img src=readme-files/testing/maximum-distance-long.png alt="Max distance is over 15"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=5>Enter goal</td>
        <td>Validate if value is empty</td>
        <td><img src=readme-files/testing/goal-empty.png alt="Goal is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not an integer</td>
        <td><img src=readme-files/testing/goal-string.png alt="Goal is not an integer"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not 5, 10, 15, or 20</td>
        <td><img src=readme-files/testing/goal-over20.png alt="Goal is not 5, 10, 15 or 20"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not more than maximum distance</td>
        <td><img src=readme-files/testing/goal-short.png alt="Goal is not more than maximum distance"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is more than 10 higher than the maxixum distance</td>
        <td><img src=readme-files/testing/goal-long.png alt="Goal is more than 10 higher than the current maximum distance"></td>
        <td>Pass</td>
    </tr>
        <tr>
        <td rowspan=2>Enter username</td>
        <td>Validate if value is not a registered username</td>
        <td><img src=readme-files/testing/enter-username-not-registered.png alt="Not a registered username"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if the user has already finished the programme</td>
        <td><img src=readme-files/testing/username-finished.png alt="User has finished the programme"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=4>Enter data</td>
        <td>Validate if value is empty</td>
        <td><img src=readme-files/testing/data-empty.png alt="Data is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not an integer</td>
        <td><img src=readme-files/testing/data-string.png alt="Data is not an integer"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if less or more than 3 values are inputted</td>
        <td><img src=readme-files/testing/data-over4.png alt="Less or more than 3 values recorded"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if any of the values are over 30</td>
        <td><img src=readme-files/testing/data-big-int.png alt="One or more values over 30"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Confirm the data</td>
        <td>Validate if value is not 'y' or 'n'</td>
        <td><img src=readme-files/testing/confirm-not-y-n.png alt="Value is not the letter 'y' or 'n'"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Return to main menu</td>
        <td>Validate if value is not 'q'</td>
        <td><img src=readme-files/testing/return-not-q.png alt="Value is not the letter 'q'"></td>
        <td>Pass</td>
    </tr>
</table>

### Solved Bugs

- It was necessary to refresh the page/re-run the programme after creating a username in order to be able to input data, as otherwise the application would not recognise the username. This also meant that it was possible to create the same username twice. This issue was fixed by assigning the list of usernames fetched from Google Sheet to a local variable instead of a global variable at the beginning.
- After returning to the main menu, it was not possible to use any of the other functions because the return_to_start function called the welcome_user function instead of the main function.
- Exception handling of the question asking the user to confirm that they have correctly inputted their running data took the user back to input their data if they entered an invalid value instead of asking again whether or not the data is correct. This was fixed by adding another while loop inside the input_data function.
- After importing Colorama, ModuleNotFoundError was received when trying to use the deployed application. This bug was solved by updating the requirements.txt file to include Colorama.

## Deployment

The application was deployed using [Heroku](https://id.heroku.com/) and Code Institute's mock terminal.

The following steps were taken to deploy this application:

1. Create requirements.txt file and run `pip3 freeze > requirements.txt` command in the terminal to create a list of requirements. Commit and push these changes to Github.
2. Go to the Heroku dashboard and click on "Create new app".
3. Once the app has been created, go to "Config Vars" under the "Settings" tab.
4. Click on "Reveals Config Vars" and in the field for KEY enter CREDS and in the field for VALUE copy-paste the entire creds.json file.
5. Add another Config Var, KEY: PORT and VALUE: 8000.
6. Go to "Buildpacks" section and set the buildpacks to `Python` and `NodeJS` in that order.
7. Go to the "Deploy" tab, select "GitHub" and click on "Connect to GitHub" and
8. Search for the repository name and click "Connect" next the repository name.
9. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

[Back to top](#run-tracker)

## Credits

### Content

All content was created by the developer.

### Media

- The ASCII art was created using [ASCII.co.uk](https://ascii.co.uk/text).

### Code

- [Geeksforgeeks](https://www.geeksforgeeks.org/how-to-make-a-table-in-python/) was consulted to learn how how to create a table in Python

- [Stackoverflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal#287944) was consulted to learn how to add colour to the text.

- Code Institute's Love Sandwiches walkthrough project inspired this project, and the steps for connecting Python to Google Sheets were taken from it.

[Back to top](#run-tracker)
