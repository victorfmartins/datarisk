import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# check the validity of the credentials
def check_creds():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES) # credentials.json is the OAuth client ID downloaded from Google Cloud
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_spreadsheet(title):
    creds = check_creds()
    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get('spreadsheetId')
    except Exception as error:
        print(f"An error occurred: {error}")
        return error

def upload_csv_to_sheet(sheet_id, file_name, sheet_name):
    creds = check_creds()
    service = build('sheets', 'v4', credentials=creds)

    # Create new sheet within the existing Spreadsheet
    spreadsheet = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    exists = False
    for s in spreadsheet['sheets']:
        if s['properties']['title'] == sheet_name:
            exists = True
    if not exists:
        body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': sheet_name
                    }
                }
            }]
        }
        service.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body=body).execute()

    # Load the CSV data into a pandas DataFrame
    df = pd.read_csv(file_name)

    # Convert the dataframe to a list of lists and include the header
    rows = df.values.tolist()
    header = df.columns.tolist()
    rows.insert(0, header)

    # Use the Sheets API to append the data
    request = service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=f'{sheet_name}!A1',
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body={'values': rows}
    )
    response = request.execute()
    print('Sheet updated successfully.')
