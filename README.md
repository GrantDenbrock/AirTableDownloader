# Airtable Downloader
Retrieves all records from an airtable database,, loads them into a df, selects a few columns, and writes those to google sheets.

# Instructions for use:

1. make a config file that looks like this:
2. Write your config file:
```python
base_id = '<xxxxxxxxxx>'
api_key = '<xxxxxxxxxx>'
table_name = '<Database Name>'
spreadsheet_name = '<Spreadsheet Name>'
filename = '<google_sheets_api_auth.json>'
```
3. main.py next to config.py and your json api creds file.

4. in terminal run ```pip3 install -r requirements.txt``` and this will install the dependenciesgit 

5. in terminal run ```python3 main.py```