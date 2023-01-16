from __future__ import print_function
from get_assignments import dueDates

import datetime
import os.path
import datefinder
import pickle
from datetime import timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
service=""

SCOPES = ['https://www.googleapis.com/auth/calendar']



def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    names,dates = dueDates()
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    

    try:
        service = build('calendar', 'v3', credentials=creds)
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=100, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', []) 
        overlap = False
        for i in range(len(names)):
            for j in events:
                if (j['start'].get('dateTime', j['start'].get('date')) == dates[i]+'T00:00:00-05:00' and j['end'].get('dateTime', j['end'].get('date'))[10:] == 'T00:00:00-05:00' and j['summary'] == names[i]):
                    overlap = True
            if overlap:
                overlap = False
                continue
            event = {
                'summary': names[i],
                'location': 'McMaster University',
                'description':'Automated Calendar Events',
                'start': {
                    'dateTime': dates[i]+'T05:00:00-00:00',
                    'timeZone': 'America/Los_Angeles',
                },
                'end': {
                    'dateTime': dates[i]+'T22:00:00-07:00',
                    'timeZone': 'America/Los_Angeles',
                },
                'recurrence': [
                    'RRULE:FREQ=DAILY;COUNT=1'
                ],
                'attendees': [
                    
                ],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                    ],
                },
            }
            event = service.events().insert(calendarId='primary', body=event).execute()


        

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['end'].get('dateTime', event['end'].get('date'))
            print(start, event['summary'])
        print(event)
    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()