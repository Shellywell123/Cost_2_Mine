#TODO
# currntly work in progress
# this python file will open all logged excel files and average values per day to calculate amount of electricity used in a month

##########################################

def get_sheet_names_between(start_date,final_date):
    """
    function to find all Cost_2_Mine log google sheets between two dates
     - looking for way to locate all sheets (shared with me) as the google api makes a sheet and shares it with your gmail account.
    """


    s_day   = int(start_date.split('/')[0])
    s_month = int(start_date.split('/')[1])
    s_year  = int(start_date.split('/')[2])

    f_day   = int(final_date.split('/')[0])
    f_month = int(final_date.split('/')[1])
    f_year  = int(final_date.split('/')[2])

    def get_days_in_month(month_num,year):
        """
        """
        if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
            num_of_days = [31,29,31,30,31,30,31,31,30,31,30,31]
            print("%d is a Leap Year" %year)
        else:
            num_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]
            print("%d is Not the Leap Year" %year)

        return num_of_days[month_num]

    assert(f_year >= s_year)

    list_of_sheet_names = []

    if s_year==f_year:
        print('htbgvfd')
        # then all days across one year

        # generate list of months through
        for month_num in range(s_month,f_month+1):
            print('btere')
            
            # set first day of month
            if month_num == s_month:
                first_day_of_the_moth = s_day
            else:
                first_day_of_the_moth = 1

            #set last day of month
            if month_num == f_month:
                last_day_of_the_month = f_day
            else:
                last_day_of_the_month = get_days_in_month(month_num,s_year)     

            # generate list of days through each month
            for day_num in range(first_day_of_the_moth,last_day_of_the_month+1):
                print('htbegrf')

                if day_num < 10:
                    day_num = '0'+str(day_num)

                if month_num < 10:
                    month_num = '0'+str(month_num)

                sheet_name = "Cost_2_Mine_log _ {}-{}-{}.csv".format(day_num,month_num,f_year)
                list_of_sheet_names.append(sheet_name)

    else:
        # days span across more than one year
        # todo
        pass



    # need to think of a way to assert strart date is beofre final date

    # need to find a way to create a list of dates between any two dates


    return list_of_sheet_names

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
sheet_names = get_sheet_names_between(start_date,final_date)
# cost_total = 0

# for sheet_name in sheet_names:

#     # scrape sheet data and average price of electricy per day for that day
#     avg = get_mean_price_per_day(sheet_name)

#     # cummaltively make a sum 
#     cost_total += avg


# from Cost_2_Mine import get_live_binance_spot_price
# tp = (get_live_binance_spot_price('DOGEGBP'))['price']
# coin_total = float(tp)*cost_total


# print('total electricty bill for period {}-{} is £{} or {} DOGE coin'.format(start_date,final_date,cost_total,coin_total))

# # get value of electricty bill in terms of current ticker price


print(sheet_names)