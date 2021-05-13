
######################################
# config variables for Cost_2_Mine
######################################
# input the varables for your setup and then rename this file to config.py


# g sheets options
gmail_address = ""

# file name options
loc_of_csv = "/some/path/to/where/you/want/the/csvs/to/save"

# tarrif options
tariff_options = {
    'post_code'       : "your postcode",
    'economy_7_meter' : True, #wether you have a economy 7 smart meter
    'pay_plan'        : 'monthly' #pay plan opts
}


# ticker info
ticker_buy = 'DOGE' #left side of ticker symbol
ticker_sell = 'GBP' #rightside of ticker symbol


# hive os login
HiveOS_username = ""
HiveOS_password = ""
access_token    = "" # generate by going into account settings in HiveOS

# unmineable
doge_address    = ""

# csv headers (make sure the values atch the headers manaually)
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
