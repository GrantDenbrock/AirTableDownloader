import requests
import csv
import pandas as pd
import config
import gspread
from gspread_dataframe import set_with_dataframe

base_id = config.base_id
api_key = config.api_key
table_name = config.table_name

# Set up the API endpoint URL
url = f'https://api.airtable.com/v0/{base_id}/{table_name}'

# Set up the request headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# make requests for data
params = ()
airtable_records = []
run = True
while run is True:
  response = requests.get(url, params=params, headers=headers)
  airtable_response = response.json()
  airtable_records += (airtable_response['records'])
  if 'offset' in airtable_response:
     run = True
     params = (('offset', airtable_response['offset']),)
  else:
     run = False

# Convert the records to a list of dictionaries
rows = [record['fields'] for record in airtable_records]

# Compile headers
headers = []
for row in rows:
    temp_list = row.keys()
    for key in temp_list:
        if key not in headers:
            headers.append(key)

# Save the records to a CSV file
with open('records.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

# Convert csv -> dataframe
df = pd.read_csv('records.csv')
df = df[['Actor ID', 'First Name', 'Last Name']]  # Adjust which columns you select here...
df.to_csv('cut_records.csv')


# export to google sheets
# gc = gspread.service_account(filename=config.filename)
gc = gspread.service_account(filename='testsheets-383317-deb0d21d757e.json')

# spreadsheet_name= config.spreadsheet_name
spreadsheet_name= 'Google API Testing'

sh = gc.open(spreadsheet_name)
worksheet = sh.get_worksheet(0)
set_with_dataframe(worksheet, df)
