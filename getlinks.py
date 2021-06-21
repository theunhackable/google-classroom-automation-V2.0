from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# CHANGE pwd
pwd = 'W:\\My Projects\\automating google classroom again\\'

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']

def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 11 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    if os.path.exists(pwd + 'token.json'):
        creds = Credentials.from_authorized_user_file(pwd + 'token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                pwd + 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(pwd + 'token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    
    try:
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])
        if not courses:
            print('\nNo courses found.')
        else:
            temp = {}
            for course in courses:
                temp[course['name']] = course['alternateLink']
        return temp
    
    except(Exception):
        print('\nError Occured. Check Your Internet Connection and try again.')
