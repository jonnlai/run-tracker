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
