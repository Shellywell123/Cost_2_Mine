import Cost_2_Mine

# make empty csv with headers 
field_names = ['Date','GBP/kWHs','Coin','Cummalative Amount','Current Value']
Cost_2_Mine.create_empty_csv(field_names)


# append entry to csv

example_entry={
        'Date':'test-date',
        'GBP/kWHs':'test-kWH',
        'Coin':'test-coin',
        'Cummalative Amount':'test-1000',
        'Current Value':'test-$100'
        }
for i in range(0,25):
    Cost_2_Mine.append_to_csv(example_entry)