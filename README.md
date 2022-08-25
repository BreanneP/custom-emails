# Custom Emails Program

## About
This program will mass-create draft emails to different users each with unique file attachments and/or unique custom fields.

## Access Instructions
* Only has to be done one time when setting up
1. Sign in to your gmail that contains the calendar you will use.
2. Navigate to [Google Console](https://console.cloud.google.com)
3. To the right of Google Cloud Platform, click New Project
4. Go through the steps to make a project.
5. Go to your project's dashboard.
6. Click the navigation menu in the top left corner.
7. Click APIs & Services --> Library.
8. Search for Calendar and click on the Gmail API.
9. Click Enable.
10. Go back to the navigation menu in the top left corner.
11. Click APIs & Services --> Credentials.
12. Click Create Credentials at the top of the screen.
13. Click OAuth client ID.
14. You will now have to go through the steps to create an OAuth consent screen. In the Scopes section, add the following scope ```https://www.googleapis.com/auth/gmail.compose```
15. When you are done with that, click Create Credentials at the top of the screen.
16. Click OAuth client ID.
17. Go through the steps of making an OAuth client ID.
18. When you are done, navigate to the Credentials dashboard.
19. Under OAuth 2.0 Client IDs, you should see the ID you just made.
20. Under Actions, you should see a download button.
21. In the popup screen that appears, click Download JSON.
22. In your downloads, rename the file to client_secret_personal.json.
23. In this directory, make a ```secrets``` folder and move client_secret_personal.json to that directory.
24. You are good to move on to the next steps below.


## Installing Requirements
* Only has to be done one time when setting up
1. Make sure that Python3 is downloaded and up-to-date
2. Open Terminal (Mac) or Command Prompt (Windows) and navigate to this directory using cd commands
3. Run the following command in Terminal/Cmd: ```pip install -r requirements.txt ```
4. You are good to move on to the next steps below.


## General Instructions
1. Write out the HTML code for the email you want drafted. For words that you want replaced for each specific email, type ```CustomField1```, ```CustomField2```, and so on
2. Copy your HTML code and paste in the ```message.txt``` file
3. Open the ```subject.txt``` file and type the subject line you want (does not have to be HTML code), using ```CustomField1```, ```CustomField2``` and so on for email-specific terminology
4. Open ```custom.csv``` in Microsoft Excel
5. In ```custom.csv```, replace each line with user-specific data. Each line corresponds to a specific email. The column ```Receiver``` should contain the email addresses
    * No file: if you don't need to send an attachment for a user, leave the ```File``` column blank
    * File: if you need to send an attachment, type the name of the file for the ```File``` column and place that file in the ```files``` folder
6. Open a Terminal (Mac) or Command Prompt (Windows)
7. Navigate to this directory using cd commands
8. Type the following in your terminal and click enter/return: ```python3 app.py```
9. The output shows you all the emails that it failed to create drafts for. If the terminal is empty, it succeeded for all your users.


## Files/Folders
* .gitignore contains all the files that Github should not commit (it is important that you do not commit your client_secret_personal.json or gmail_personal.csv files)
* app.py is the application that verifies credentials and calls the other files' functions
* client_secret_personal.json contains your Google OAuth client secrets
* creds.py is the script to generate your scope-specific credentials
* custom.csv contains all the email-specific data you want in your drafts
* emails.py handles working with the Gmail API and drafting messages
* files folder contains all the file attachments you will attach in your drafts
* message.py is the script used to make the HTML messages
* message.txt contains the HTML of the email_content
* README.md is this file you're reading right now
* requirements.txt contains all the requirements you will need for this program
* secrets folder contains client_secret_personal.json and (after running the script once) gmail_personal.json
* subject.txt contains the text of the subject line

## Sources
* [Gmail Send Example](https://stackoverflow.com/questions/37201250/sending-email-via-gmail-python
)
* [Stack Overflow](https://stackoverflow.com/)
* [Draft Gmail Messages](https://developers.google.com/gmail/api/guides/drafts)
* [Draft Scopes](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create)
