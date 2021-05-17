#TODO
# currntly work in progress
# this python file will open all logged excel files and average values per day to calculate amount of electricity used in a month


def get_sheets_between(start_date,final_date):
    """
    function to find all Cost_2_Mine log google sheets between two dates
     - looking for way to locate all sheets (shared with me) as the google api makes a sheet and shares it with your gmail account.
    """
    pass

def get_sheet_data(sheet_id):
    """
    function to retrieve a sheets data once supplied a form of id
     - currently playing with id's either by key or url
     - may add an argument to extract by coloumn
    """
    pass

def get_mean_price_per_day(sheet):
    """
    function to extract the average price per day as the logger calculates it on the fly with every entry
    """

    # first index price per day column in data
    data = 

    # 2nd mean that data
    for value in data:
        value = float(value)

    import numpy
    day_mean = numpy.mean(data)

    # return mean
    return day_mean

##########################################
# how I envisage the code being used
##########################################

# download/ open google sheets

start_date = '1/1/2020'
final_date = '1/2/2020'
sheet_ids = get_sheets_between(start_date,final_date)

cost_total = 0

for sheet_id in sheet_ids:

    # scrape sheet data
    sheet_data = get_sheet_data(sheet_id)

    # average price of electricy per day for that day
    avg = get_mean_price_per_day(sheet_data)

    # cummaltively make a sum 
    cost_total += avg

print('total electricty bill for period {}-{}  is {}'.format(start_date,final_date,cost_total))

# get value of electricty bill in terms of current ticker price
from Cost_2_Mine import get_live_binance_spot_price
tp = get_live_binance_spot_price('DOGEGBP')
cost_total_crypto = float(tp)*cost_total



