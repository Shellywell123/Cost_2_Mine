import Cost_2_Mine
from datetime import datetime
from config import *
import threading
import time
 
ticker = ticker_buy+ticker_sell


########################################################################################


def choose_preset_by_ticker(ticker):
    """
    """

    if ticker == 'DOGEGBP':
        auto_log_DOGE_preset()

    else:
        print('currently no preset for this ticker, please try a differnent ticker of make a preset')


########################################################################################
# ticker presets
########################################################################################

def auto_log_DOGE_preset():
    """
    """
    entry_every_N_mins = 1
    minute = 60
    threading.Timer(entry_every_N_mins*minute, auto_log_DOGE_preset).start()

    #######################################################
    # calculating dict values for csv entry
    #######################################################

    #file name
    from datetime import datetime
    date = datetime.now().strftime("%d-%m-%Y")
    name_of_g_sheet = "{}.csv".format("Cost_2_Mine_log _ "+date)

    # test connection
    if Cost_2_Mine.check_internet_connection() == 'no internet':
        print('not connected to the internet ... retrying')
        time.sleep(3)
        auto_log_DOGE_preset()

    # scrape data
    try:
        unMinable_data         = dict(Cost_2_Mine.get_live_unMinable_data()) # do unmineable data 1st as has a loop til completion
    except:
        print( ' - unMineable scrape error ... retrying')
        unMinable_data         = dict(Cost_2_Mine.get_live_unMinable_data()) 

    try:
        HiveOS_data            = dict(Cost_2_Mine.get_live_HiveOS_data())
    except:
        print( ' - HiveOS scrape error ... retrying')
        HiveOS_data            = dict(Cost_2_Mine.get_live_HiveOS_data())

    try:
        ticker_data            = Cost_2_Mine.get_live_binance_spot_price(ticker)
    except:
        print( ' - binance api scrape error ... retrying')
        ticker_data            = Cost_2_Mine.get_live_binance_spot_price(ticker)

    try:
        tariff_data = Cost_2_Mine.get_live_kWhs_from_Bulb()
    except:
        print( ' - tariff scrape error ... retrying')
        tariff_data = Cost_2_Mine.get_live_kWhs_from_Bulb()

    
    # index data
    date                   = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    price_per_kWh          = tariff_data
    power_consumption      = HiveOS_data['stats']['power_draw']
    ticker_value           = ticker_data['price']
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
    day_gross              = (float(day_net) - float(day_cost)) * (1 - (float(payout_fee)/100))
    
    # populate dict (make sure the values atch the headers manaually)
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

    Cost_2_Mine.create_append_to_g_sheets(name_of_g_sheet,entry)

    print('waiting {} minutes til next auto entry'.format(entry_every_N_mins))
  

########################################################################################


print("""
#####################################################
#            Cost_2_Mine Initiating                 #
#####################################################
""")

choose_preset_by_ticker(ticker)