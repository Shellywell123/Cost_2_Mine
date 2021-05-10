# Cost_2_Mine
Python project that genertes a live balance sheet for mining crypto via HiveOS by scraping live ticker prices and electrictity tariffs.

 - `N.B. I am writing this for my specific setup, Bulb energy supplier and HiveOS mining` 
 - make entries to speadsheet at timed intervals - currently under development
 - I plan to make a function per ticker I mine, as some tickers have mined coins in other pool pages than HiveOS.

## Usage 
open `example-config.py` and change the variables for your setup. Then rename `example-config.py` to `config.py`. You will need an access token to access your live HiveOS data, this is easily done by creating an access token in the settings page of HiveOS dashboard. You may need to tweak the code for csv entries in `run.py` too suit your needs. Then execute the program:

```py
python3 run.py
```