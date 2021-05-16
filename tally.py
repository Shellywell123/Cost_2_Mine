#TODO
# currntly work in progress
# this python file will open all logged excel files and average values per day to calculate amount of electricity used in a month


def get_sheets(start_date,final_date):
    """
    """
    pass

# download/ open google sheets

start_date = '1/1/2020'
final_date = '1/2/2020'
sheets = get_sheets(start_date,final_date)

cost_total = 0

for sheet in sheets:

    # average price of electricy per day for that day
    avg = None

    # cummaltively make a sum 
    cost_total += avg

print('total electricty bill for period {}-{}  is {}'.format(start_date,final_date,cost_total))

# get value of electricty bill in terms of current ticker price
from Cost_2_Mine import get_live_binance_spot_price
tp = get_live_binance_spot_price('DOGEGBP')
cost_total_crypto = float(tp)*cost_total



