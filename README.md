# Run Tracker

![Mockup image](readme-files/mockup-image.png)

Run tracker allows users to learn to run 5-20 kilometers. The application recommends the user a training plan and allows then track and view their progress.

The deployed project can be found here: [Run Tracker](https://running-programme-694cea56c7e6.herokuapp.com/)

## User Experience (UX)

### Project Goals

- Help users to improve their fitness level by providing users an easy way to start running or to increase the distance they can run.
- Allow users to track their their progress for the duration of the programme.
- Validate the data the user inputs to ensure that the programme works correct and provides good user experience.

### User Stories

- As someone new to running, I want an easy to follow plan that gives me the weekly structure that I need in order to be able to start running.
- As a beginner or intermediate runner, I want a programme that helps me to push my limits and get better results.
- As a user of the application, I want to be able to store my running data.
- As a user of the application, I want to be able to view my progress and compare that to my plan.

### Flowchart

A flowchart to plan the logic of the programme was created using [Lucid](https://lucid.app/).

![Flowchart](readme-files/flowchart.png)

### Data Model

The data that user inputs is initially stored as variables. Once all the necessary data has been inputted by the user and it has been validated, the data is added to a Google Sheets.

Three worksheets are being used:

- one to store the four different running plans that the programme offers
- one to store which plan each user had chosen
- one to store the user's running data

[Back to top](#run-tracker)

## Features

### Main page

The user is given information about the application and is asked to select an option.

![Main page](readme-files/mockup-image.png)

### Select plan

Collects information from the user in order to be able to select the most suitable plan for them based on the maximum distance that the user can currently run and their goal. Adds the username and the user's select plan to Google Sheets.

![Select plan](readme-files/features/select-plan.png)

### View plan

Displays the selected 8-week plan to the user and advises user when to return to input their results.

![View plan](readme-files/features/view-plan.png)

### Input data

Asks the user to input their username and if the username is recognised, allows the user to input previous week's running data.

![Input data](readme-files/features/input-data.png)

### Next week's plan

After the user has added their latest running data, next week's plan is displayed to user, and their encouraged to keep following the running programme and to return the following week to add that week's results.

![Next week](readme-files/features/next-week.png)

### Programme finished

Inform the user that they have finished the programme and advises them to how they can view their results.

![Programme finished](readme-files/features/programme-finished.png)

### View progress

Asks the user to input their username and if the username is recognised, allows the user to view their results and their plan.

![View progress](readme-files/features/view-progress.png)

[Back to top](#run-tracker)

## Technologies Used

### Language Used

- [Python3](https://www.python.org/)

### Frameworks, Libraries and Programs Used

- [Lucid](https://lucid.app/) was used to create the programme flowchart.

- [VSCode](https://code.visualstudio.com/) was used for writing code, committing, and then pushing to GitHub.

- [GitHub](https://github.com/) was used to store the project after pushing.

- [Heroku](https://id.heroku.com/) was used to deploy the application.

- [CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code.

- [Tabulate](https://pypi.org/project/tabulate/) library was used to present the data in a table format.

- [Colorama](https://pypi.org/project/colorama/) library was used to apply color to the terminal text.

[Back to top](#run-tracker)

## Testing

### Code Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code for PEP8 requirements.

The code was validated for the first time, the following warning and error messages were received.

![Python Linter 1](readme-files/python-linter/python-linter-1.png)
![Python Linter 2](readme-files/python-linter/python-linter-2.png)
![Python Linter 3](readme-files/python-linter/python-linter-3.png)
![Python Linter 4](readme-files/python-linter/python-linter-4.png)
![Python Linter 5](readme-files/python-linter/python-linter-5.png)
![Python Linter 6](readme-files/python-linter/python-linter-6.png)
![Python Linter 7](readme-files/python-linter/python-linter-7.png)
![Python Linter 8](readme-files/python-linter/python-linter-8.png)
![Python Linter 9](readme-files/python-linter/python-linter-9.png)

The warnings and errors were addressed and it was confirmed that no errors remained.

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
        <td>Validate if value is number other than 1, 2 or 3</td>
        <td><img src=readme-files/testing/select-option-num-test.png alt="Value is number not 1,2,3"></td>
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
        <td>Select option</td>
        <td>Select option</td>
        <td>Select option</td>
        <td>Select option</td>
    </tr>
</table>

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

- [Stackoverflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal#287944) was consulted to learn how to add color to the text

- Code Institute's Love Sandwiches walkthrough project inspired this project and the steps of how to connect Python to Google Sheets were taken from it.
