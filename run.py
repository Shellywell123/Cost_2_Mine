import Cost_2_Mine
from datetime import datetime
from config import *
 
ticker = ticker_buy+ticker_sell

# make empty csv with headers 
field_names = [
    'Date',
    '{}/kWHs'.format(ticker_sell),
    'Power Consumption W','Ticker',
    'Ticker Value',
    'Hashrate MH/s',
    'Mined til Payout',
    'Total Paidout',
    'Payout Fee',
    'is auto payout checked',
    'Total {}'.format(ticker_buy),
    'Total Value {}'.format(ticker_sell),
    '{}/day Bill'.format(ticker_sell),
    '{}/day Net'.format(ticker_sell),
    '{}/day Gross'.format(ticker_sell)
    ]

Cost_2_Mine.create_empty_csv(field_names)

# append entry to csv in loop as dev example

for i in range(0,25): # will replace this with a timed interval so I get regular entries

    # calculating dict values for csv entry
    date                   = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    price_per_kWh          = '0.1503'#to-be-scraped
    power_consumption      = Cost_2_Mine.get_live_HiveOS_data()['stats']['power_draw']
    ticker_value           = Cost_2_Mine.get_live_price(ticker)['price']
    total_amount           = 420 # to be scraped
    total_value            = float(ticker_value)*float(total_amount)
    day_cost               = float(price_per_kWh)*float(power_consumption)*(24/1000)
    hashrate               = float(Cost_2_Mine.get_live_HiveOS_data()['hashrates'][0]['hashrate']/1000) #MH/s
    mined_til_payout       = Cost_2_Mine.get_live_unMinable_data()['mined_til_payout']
    mined_in_last_24hrs    = Cost_2_Mine.get_live_unMinable_data()['mined in last 24hrs']
    day_net                = float(mined_til_payout)*float(price_per_kWh)
    total_paidout          = Cost_2_Mine.get_live_unMinable_data()['total_paidout']
    last_payout_date       = Cost_2_Mine.get_live_unMinable_data()['last_payout_date']
    payout_fee             = Cost_2_Mine.get_live_unMinable_data()['payout_fee']
    is_auto_payout_checked = Cost_2_Mine.get_live_unMinable_data()['is_auto_payout_checked']
    day_gross              = (float(day_net) - float(day_cost)) * (1 - float(payout_fee[:-1]))

    # populate dict
    example_entry={
        'Date':date,
        '{}/kWHs'.format(ticker_sell)        : price_per_kWh,
        'Power Consumption W'                : power_consumption,
        'Ticker'                             : ticker,
        'Ticker Value'                       : ticker_value,
        'Hashrate MH/s'                       : hashrate,
        'Mined til Payout'                   : mined_til_payout,
        'Total Paidout'                      : total_paidout,
        'Payout Fee'                         : payout_fee,
        'is auto payout checked'             : hashrate,
        'Total {}'.format(ticker_buy)        : mined_til_payout, #using mined til payout as disabled autopayout
        'Total Value {}'.format(ticker_sell) : total_value,
        '{}/day Bill'.format(ticker_sell)    : day_cost,
        '{}/day Net'.format(ticker_sell)     : day_net,
        '{}/day Gross'.format(ticker_sell)   : day_gross,
        }

    Cost_2_Mine.append_to_csv(example_entry)