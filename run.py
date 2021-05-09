import Cost_2_Mine
from datetime import datetime
from config import *
 
ticker = ticker_buy+ticker_sell

# make empty csv with headers 
field_names = ['Date','{}/kWHs'.format(ticker_sell),'Power Consumption','Ticker','Ticker Value','Total {}'.format(ticker_buy),'Total Value {}'.format(ticker_sell)]
Cost_2_Mine.create_empty_csv(field_names)

# append entry to csv in loop as dev example

for i in range(0,25):

    # calculating dict values for csv entry
    date              = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    price_per_kWh     = 'to-be-scraped'
    power_consumption = 'to-be-scraped'
    ticker_value      = Cost_2_Mine.get_live_price(ticker)['price']
    total_amount      = 420 # to be scraped
    total_value       = float(ticker_value)*float(total_amount)

    # populate dict
    example_entry={
        'Date':date,
        '{}/kWHs'.format(ticker_sell)        : price_per_kWh,
        'Power Consumption'                  : power_consumption,
        'Ticker'                             : ticker,
        'Ticker Value'                       : ticker_value,
        'Total {}'.format(ticker_buy)        : total_amount,
        'Total Value {}'.format(ticker_sell) : total_value
        }

    Cost_2_Mine.append_to_csv(example_entry)