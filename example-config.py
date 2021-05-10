
######################################
# config variables for Cost_2_Mine
######################################
# input the varables for your setup and then rename this file to config.py

# file name options
name_of_csv = "Mining_Balance_Sheet.csv"

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
doge_address = ""