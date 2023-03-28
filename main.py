import requests
import csv

# Replace with your own values
base_id = 'YOUR_BASE_ID'
api_key = 'YOUR_API_KEY'
table_name = 'YOUR_TABLE_NAME'

# Set up the API endpoint URL
url = f'https://api.airtable.com/v0/{base_id}/{table_name}'

# Set up the request headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Make the request to the Airtable API
response = requests.get(url, headers=headers)

# Parse the JSON response
records = response.json()['records']

# Convert the records to a list of dictionaries
rows = [record['fields'] for record in records]

# Extract the headers from the first record
headers = rows[0].keys()

# Save the records to a CSV file
with open('records.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)
