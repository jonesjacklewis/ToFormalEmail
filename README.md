# To Formal Email

## Overview

- This project has a number of different clients/integrations and is designed to take an informal prompt and return a formal email.
- Use cases include helping people with lower experience in writing formal communications/with lower levels of literacy
- An example prompt is below:

```
Hi - I am interested at the job at MadeUpCompany for the role of tester. I have a couple years in this type of role and want to learn more. I like what your company does. Thanks - John Smith
```

- An example of a response generated is below:

```
Subject: Interest in Tester Role at MadeUpCompany

Dear Hiring Team at MadeUpCompany, 

My name is John Smith and I am writing in regards to the Tester role at your company. I have a couple of years of experience in this type of role and am eager to learn more. After researching your company, I am very impressed and interested in what you do. 

I am confident that I have the skills and knowledge to be a great asset to your team and am available for an interview anytime. If you have any questions or need further information, please do not hesitate to contact me. 

Thank you for your time. 

Sincerely, 
John Smith
```

- Below is the outline of the different components in this project

## main.py

- This powers the other components of the project.
- A generically writen service to integrate with the openai platform
- Reads config files
- Takes a string and through interfacing with openai converts it into a formal email.

## discord-bot.py

- This is an integration with the instant messaging platform discord
- Uses the main.py core functionality
- As a deployed discord bot, when the program is running, will work on each of the discord servers it runs on.

## twilio-sms-bot.py

- This is an integration with the platform Twilio, this allows for integration with SMS messages

## gui.py

- A graphical user interface that integrates with the core functionality of main.py
- Uses PyQt6
