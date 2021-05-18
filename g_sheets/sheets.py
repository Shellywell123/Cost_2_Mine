
from __future__ import print_function
from g_sheets.auth import spreadsheet_service
from g_sheets.auth import drive_service
from config import gmail_address

def create(sheet_title):
    spreadsheet_details = {
    'properties': {
        'title': sheet_title
        }
    }
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details,
                                    fields='spreadsheetId').execute()
    sheetId = sheet.get('spreadsheetId')
    print('Spreadsheet ID: {0}'.format(sheetId))
    permission1 = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': gmail_address
    }
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()
    print('{} sheet made!'.format(sheet_title))
    return sheetId


def get_sheet_data(sheet_name):
    """
    function to retrieve a sheets data once supplied a form of id
     - currently playing with id's either by key or url
     - may add an argument to extract by coloumn
    """
    from g_sheets.auth import credentials
    import gspread
    client = gspread.authorize(credentials)
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()

    return data
