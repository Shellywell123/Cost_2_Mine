#TODO
# currntly work in progress
# this python file will open all logged excel files and average values per day to calculate amount of electricity used in a month

##########################################

def get_sheet_names_between(start_date,final_date):
    """
    function to find all Cost_2_Mine log google sheets between two dates
     - looking for way to locate all sheets (shared with me) as the google api makes a sheet and shares it with your gmail account.
    """

    # unpack date data
    s_day   = int(start_date.split('/')[0])
    s_month = int(start_date.split('/')[1])
    s_year  = int(start_date.split('/')[2])

    f_day   = int(final_date.split('/')[0])
    f_month = int(final_date.split('/')[1])
    f_year  = int(final_date.split('/')[2])

    # assertion check date data
    assert(0 < s_day < 32) 
    assert(0 < f_day < 32) 
    assert(0 < s_month < 13) 
    assert(0 < f_month < 13) 
    assert(f_year >= s_year)

    def get_days_in_month(month_num,year):
        """
        """
        if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
            num_of_days = [31,29,31,30,31,30,31,31,30,31,30,31]
            print("%d is a Leap Year" %year)
        else:
            num_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]
            print("%d is Not the Leap Year" %year)

        return num_of_days[month_num-1]

    list_of_sheet_names = []

    for year_num in range(s_year,f_year+1):

        # then all days across one year

        # set first day of month
        if year_num == s_year:
            first_month_of_the_year = s_month
        else:
            first_month_of_the_year = 1

        #set last day of month
        if year_num == f_year:
            last_month_of_the_year = f_month
        else:
            last_month_of_the_year = 12

        # generate list of months through
        for month_num in range(first_month_of_the_year,last_month_of_the_year+1):
            
            # set first day of month
            if month_num == s_month:
                first_day_of_the_month = s_day
            else:
                first_day_of_the_month = 1

            #set last day of month
            if month_num == f_month:
                last_day_of_the_month = f_day
            else:
                last_day_of_the_month = get_days_in_month(month_num,year_num)     

            assert(type(month_num) == int)
            # generate list of days through each month
            for day_num in range(first_day_of_the_month,last_day_of_the_month+1):

                if day_num < 10:
                    day_num = '0'+str(day_num)

                month_num = int(month_num)
                if month_num < 10:
                    month_num = '0'+str(month_num)

                sheet_name = "Cost_2_Mine_log _ {}-{}-{}.csv".format(day_num,month_num,year_num)
                
                #print(sheet_name)
                list_of_sheet_names.append(sheet_name)

    return list_of_sheet_names

##########################################

def get_mean_bill_per_day(fiat_name,sheet_name):
    """
    function to extract the average price per day as the logger calculates it on the fly with every entry
    """

    from g_sheets.sheets import get_sheet_data
    sheet_data = get_sheet_data(sheet_name)


    # first index price per day column in data
    ppd = []
    for entry in sheet_data:
        try:
            ppd.append(float(entry['{}/day Electricity'.format(fiat_name)]))
        except:
            pass

    import numpy as np
    day_mean = np.mean(ppd)

    # return mean
    return day_mean

##########################################

def get_mean_prof_on_day(fiat_name,sheet_name):
    """
    function to extract the profit per day as the logger calculates it on the fly with every entry
    """

    from g_sheets.sheets import get_sheet_data
    sheet_data = get_sheet_data(sheet_name)


    # first index price per day column in data
    ppd = []
    for entry in sheet_data:
        try:
            ppd.append(float(entry['{}/day Gross'.format(fiat_name)]))
        except:
            pass

    import numpy as np
    day_mean = np.mean(ppd)

    # return mean
    return day_mean

##########################################

def get_mean_coin_amount_on_day(coin_name,sheet_name):
    """
    function to extract the profit per day as the logger calculates it on the fly with every entry
    """

    from g_sheets.sheets import get_sheet_data
    sheet_data = get_sheet_data(sheet_name)


    # first index price per day column in data
    ppd = []
    for entry in sheet_data:
        try:
            ppd.append(float(entry['Total {}'.format(coin_name)]))
        except:
            pass

    import numpy as np
    day_mean = np.mean(ppd)

    # return mean
    return day_mean


##########################################


def tally_g_sheets(start_date,final_date,coin_name,fiat_name):
    """
    summarise expenses of g_sheets between two dates
    """

    print("""
############################################################################
#         Cost_2_Mine Summary for Period {}-{}             #
############################################################################
""".format(start_date,final_date))

    sheet_names = get_sheet_names_between(start_date,final_date)

    ######################
    # get profit summary
    ######################

    start_coin = get_mean_coin_amount_on_day(coin_name,sheet_names[0])
    end_coin   = get_mean_coin_amount_on_day(coin_name,sheet_names[-1])

    mined_coin = end_coin-start_coin

    print(' - total mined is {} {}'.format(mined_coin,coin_name))


    ######################
    # get bill summary
    ######################


    bill_gbp_total = 0
    profit_gbp_total = 0
    for sheet_name in sheet_names:

        # scrape sheet data and average price of electricy per day for that day
        bill_avg = get_mean_bill_per_day(fiat_name,sheet_name)

        #print(sheet_name,bill_avg)

        # cummaltively make a sum 
        bill_gbp_total += bill_avg


    from Cost_2_Mine import get_live_binance_spot_price
    coin_price = (get_live_binance_spot_price(coin_name+fiat_name))['price']
    bill_coin_total = bill_gbp_total/float(coin_price)


    profit_gbp_total = float(mined_coin)*float(coin_price) - bill_gbp_total

    print(' - total profit is {} {}'.format(profit_gbp_total,fiat_name))


    #of you get nan as a value it may be due to one of your sheets not having headers
    print(' - total electricty bill is {} {} or {} {} coin'.format(bill_gbp_total,fiat_name,bill_coin_total,coin_name))

##########################################
# how I envisage the code being used
##########################################

start_date = '15/05/2021'
final_date = '20/05/2021'

coin_name = 'DOGE'
fiat_name = 'GBP'

tally_g_sheets(start_date,final_date,coin_name,fiat_name)