# Cost_2_Mine
Python project made to generte a balance sheet for mining crypto via HiveOS via scraping live ticker prices and electrictity tarrifs.

 - `N.B. I am writing this for my specific setup, Bulb energy supplier and HiveOS mining` 
 - still need to fix bulb tarrif scraper
 - make entries to speadsheet at timed intervals
 - I will make a function per ticker I mine as some tickers have mined coins in other pool pages than HiveOS.
 - seems to be a subscript error on occasion of scraping unmineable (think I need to playaround with timeout)

## Usage 
open `example-config.py` and change the variables for your setup. Then rename `example-config.py` to `config.py`. You will need an access token to access your live HiveOS data, this is easilt done by creating an access token in the settings page of HiveOS dashboard. Then execute the program:

```py
python3 run.py
```