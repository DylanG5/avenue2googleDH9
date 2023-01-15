# avenue2googleDH9
Authors: Harman Bassi, Dylan Garner, Matthew Bradbury, Aswin Kuganesan
Devpost: https://devpost.com/software/a2g?ref_content=my-projects-tab&ref_feature=my_projects

This program is designed to input the user's assignments into their Google Calendar automatically. We thought of this idea because we did not like having to manually input our assignments into Google Calendar, which is our main calendar/planner. Since our assignments are on Avenue to Learn, we could use web scraping to extract our assignments from Avenue, and use the Google Calendar API to automatically input it onto the calendar.

In order to add your assignments to Google Calendar, you need to implement the requirements in the requirements.txt, since you need to set up the libraries and venv. Then, fill out your Avenue credentials and run the eventAdder code. This code will ask your Google account for permissions to allow the API to add events to your calendar. After giving the API access one time you will not need to authenticate your account. After automatically logging into your Avenue, you will be required to do 2 factor authentication on your authenticator app and then the assignments will be extracted from your Avenue account and transferred onto Google Calendar.

