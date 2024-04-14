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

The data that user inputs is initially stored as variables. Once all the necessary data has been inputted by the user and it has been validated, the data is added to a Google Sheet.

Three worksheets are being used:

- one to store the four different running plans that the programme offers
- one to store which plan each user had chosen
- one to store the user's running data
