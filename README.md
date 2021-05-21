# Cost_2_Mine (Mine-Your-Own-Business)
Python project that generates a live balance sheet for mining crypto via HiveOS, by scraping live ticker prices and electricity tariffs.

 - `N.B. I am writing this for my specific setup, Bulb energy supplier and HiveOS mining` 
 - I plan to make a function/preset per HiveOS flightsheet

## Usage 
 - Open `example-config.py` and change the variables for your setup.
 - Then rename `example-config.py` to `config.py`.
 - You will need an access token to access your live HiveOS data, this is easily done by creating an access token in the settings page of HiveOS dashboard. 
 - You may need to tweak the code for csv entries in `run.py` too suit your needs. 
 - The program currently collects and appends data to a csv every 1 minute, tis vaule can be found and changed in the presets of `auto_logger.py` 
 - if left runnning the script will make a new csv every time the date changes
 - script can be used to write to local csv files or google sheets (`g-sheets` scripts where found from [here](https://blog.coupler.io/python-to-google-sheets/))

 Then execute the program:

```py
python3 auto_logger.py
```
```bash
#####################################################
#            Cost_2_Mine Initiating                 #
#####################################################
```
[program will then print out each entry of the csv as it collects the live data]
