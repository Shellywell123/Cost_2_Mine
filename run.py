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
    'To be paidout {}'.format(ticker_buy) ,
    'Minimum payout {}'.format(ticker_buy) ,
    'Total Paidout {}'.format(ticker_buy) ,
    'Payout Fee',
    'Auto payout status',
    'Total {}'.format(ticker_buy),
    'Total Value {}'.format(ticker_sell),
    '{}/day Electricity'.format(ticker_sell),
    '{}/day Net'.format(ticker_sell),
    '{}/day Gross'.format(ticker_sell)
    ]

Cost_2_Mine.create_empty_csv(field_names)

# append entry to csv in loop as dev example
if ticker == 'DOGEGBP':
    for i in range(0,25): # will replace this with a timed interval so I get regular entries

        #######################################################
        # calculating dict values for csv entry
        #######################################################

        # scrape data
        unMinable_data         = Cost_2_Mine.get_live_unMinable_data() # do unmineable data 1st as has a loop til completion
        HiveOS_data            = Cost_2_Mine.get_live_HiveOS_data()
        
        # index data
        date                   = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        price_per_kWh          = Cost_2_Mine.get_live_kWhs_from_Bulb()
        power_consumption      = HiveOS_data['stats']['power_draw']
        ticker_value           = Cost_2_Mine.get_live_price(ticker)['price']
        to_be_paidout          = unMinable_data['pending_mining_balance']
        total_paidout          = unMinable_data['total_paid']
        last_payout_date       = unMinable_data['last_payment_date']
        payout_fee             = 0.75 # couldnt scrape this as is a reduced fee
        is_auto_payout_checked = unMinable_data['auto_pay']
        hashrate               = float(HiveOS_data['hashrates'][0]['hashrate']/1000) #MH/s
        mined_in_last_24hrs    = unMinable_data['total_24h']
        minimum_payout         = unMinable_data['payment_threshold']

        # calculations
        total_amount           = float(to_be_paidout) + float(total_paidout)
        total_value            = float(ticker_value)*float(total_amount)
        day_cost               = float(price_per_kWh)*float(power_consumption)*(24/1000)
        day_net                = float(mined_in_last_24hrs)*float(price_per_kWh)
        day_gross              = (float(day_net) - float(day_cost)) * (1 - (float(payout_fee[:-1])/100))
        
        # populate dict
        entry={
            'Date':date,
            '{}/kWHs'.format(ticker_sell)          : price_per_kWh,
            'Power Consumption W'                  : power_consumption,
            'Ticker'                               : ticker,
            'Ticker Value'                         : ticker_value,
            'Hashrate MH/s'                        : hashrate,
            'To be paidout {}'.format(ticker_buy)  : to_be_paidout,
            'Minimum payout {}'.format(ticker_buy) : minimum_payout,
            'Total Paidout {}'.format(ticker_buy)  : total_paidout,
            'Payout Fee'                           : payout_fee,
            'Auto payout status'                   : is_auto_payout_checked,
            'Total {}'.format(ticker_buy)          : total_amount, 
            'Total Value {}'.format(ticker_sell)   : total_value,
            '{}/day Electricity'.format(ticker_sell)      : day_cost,
            '{}/day Net'.format(ticker_sell)       : day_net,
            '{}/day Gross'.format(ticker_sell)     : day_gross,
            }

        Cost_2_Mine.append_to_csv(entry)