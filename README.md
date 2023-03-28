# Instructions

Replace the 3 values at the top with your own values and run:

```commandline
python main.py
```

It should generate a csv file called records.csv

You may/may not need to install requests. IF you do, you just need to run:
```commandline
pip install requests
```

and then run the script again.

OR alternatively, you could just run: ```curl "https://api.airtable.com/v0/{baseID}/{tableName}?api_key={apiKey}" > records.json
```

Which would get you your database dump in json format instead of csv if that is helpful...
