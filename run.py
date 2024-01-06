import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# all this code above is just for me to access my spreadsheet data

def get_sales_data():
    """
    Get sales figures input from the user, write with print() because it will be displaied as in a terminal
    """

    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n") # das n mit dem backslash ist für styling Effekte gut

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_sales_data()