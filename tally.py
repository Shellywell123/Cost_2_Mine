#TODO
# currntly work in progress
# this python file will open all logged excel files and average values per day to calculate amount of electricity used in a month

##########################################

def get_sheet_names_between(start_date,final_date):
    """
    function to find all Cost_2_Mine log google sheets between two dates
     - looking for way to locate all sheets (shared with me) as the google api makes a sheet and shares it with your gmail account.
    """

    s_day = start_date.split('/')[0]
    s_month = start_date.split('/')[1]
    s_year = start_date.split('/')[2]

    f_day = final_date.split('/')[0]
    f_month = final_date.split('/')[1]
    f_year = final_date.split('/')[2]

    assert(f_year >= s_year)
    # need to think of a way to assert strart date is beofre final date

    # need to find a way to create a list of dates between any two dates
    day = 0
    month = 0
    year = 0

    naming_convetion = "Cost_2_Mine_log _ {}-{}-{}.csv".format(day,month,year)

    sheet_names = 0

    return sheet_names

##########################################

def get_mean_price_per_day(sheet_name):
    """
    function to extract the average price per day as the logger calculates it on the fly with every entry
    """

    from g_sheets.sheets import get_sheet_data
    sheet_data = get_sheet_data(sheet_name)

    # first index price per day column in data
    ppd = []
    for entry in sheet_data:
        try:
            ppd.append(float(entry['GBP/day Electricity']))
        except:
            pass

    import numpy as np
    day_mean = np.mean(ppd)

    # return mean
    return day_mean

##########################################
# how I envisage the code being used
##########################################

# download/ open google sheets

start_date = '15/05/2020'
final_date = '16/05/2020'
#sheet_names = get_sheets_names_between(start_date,final_date)
sheet_names = ["Cost_2_Mine_log _ 15-05-2021.csv","Cost_2_Mine_log _ 16-05-2021.csv"]
cost_total = 0

for sheet_name in sheet_names:

    # scrape sheet data and average price of electricy per day for that day
    avg = get_mean_price_per_day(sheet_name)

    # cummaltively make a sum 
    cost_total += avg


from Cost_2_Mine import get_live_binance_spot_price
tp = (get_live_binance_spot_price('DOGEGBP'))['price']
coin_total = float(tp)*cost_total


print('total electricty bill for period {}-{} is £{} or {} DOGE coin'.format(start_date,final_date,cost_total,coin_total))

# get value of electricty bill in terms of current ticker price



