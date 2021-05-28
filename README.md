# Cost_2_Mine (Mine-Your-Own-Business)
Python project that generates a live balance sheet for mining crypto via HiveOS, by scraping live ticker prices and electricity tariffs.

 - `N.B. I am writing this for my specific setup, Bulb energy supplier and HiveOS mining` 
 - I plan to make a function/preset per HiveOS flightsheet

## Setup:
 - Open `example-config.py` and change the variables for your setup.
 - Then rename `example-config.py` to `config.py`.
 - You will need an access token to access your live HiveOS data, this is easily done by creating an access token in the settings page of HiveOS dashboard. 
 - You may need to tweak the code for csv entries in `run.py` too suit your needs. 
 - The program currently collects and appends data to a csv every 1 minute, tis vaule can be found and changed in the presets of `auto_logger.py` 
 - if left runnning the script will make a new csv every time the date changes
 - script can be used to write to local csv files or google sheets (`g-sheets` scripts where found from [here](https://blog.coupler.io/python-to-google-sheets/))

## Usage:
### To generate csv log files:

```py
python3 auto_logger_g_sheets.py
#or
python3 auto_logger_local.py
```

```bash
#####################################################
#            Cost_2_Mine Initiating                 #
#####################################################
```
[program will then print out each entry of the csv as it collects the live data]
 - N.B If you are using `UnMineable.com` to view hasrates etc, the generated `net profit per day` is based apon the 'Last 24hr Reward' on the 'unmineable dash', i.e dont worry if your net profit is negative for the first 24 hours of starting the rig.

### To summarise log files:
 - curently only written for google-sheets
 - open and edit `tally.py` for you own paramaters

```py
python3 tally.py
```
[program will then average and total up values in each sheet, DOGE example below]

```bash

############################################################################
#         Cost_2_Mine Summary for Period 15/05/2021-20/05/2021             #
############################################################################

 - total mined is ... DOGE
 - total profit is £...
 - total electricty bill is £... or ... DOGE coin
 ```
