import Cost_2_Mine
import config
from datetime import datetime
 

# make empty csv with headers 
field_names = ['Date','GBP/kWHs','Power Consumption','Ticker','Cummalative Amount','Current Value']
Cost_2_Mine.create_empty_csv(field_names)


# append entry to csv in loop as dev example
ticker = 'DOGEGBP'

for i in range(0,25):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    example_entry={
        'Date':dt_string,
        'GBP/kWHs':'test-kWH',
        'Power Consumption':'test-pc',
        'Ticker':ticker,
        'Cummalative Amount':'test-1000',
        'Current Value':Cost_2_Mine.get_live_price(ticker)['price']
        }

    Cost_2_Mine.append_to_csv(example_entry)