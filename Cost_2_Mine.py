import csv
from config import *

############################################################

def print_html(html_str):
   """
   prints html code  with correct formating
   """
   from bs4 import BeautifulSoup
   print(BeautifulSoup(html_str, 'html.parser').prettify())


############################################################

def scrape_kWhs_from_Bulb(post_code):
    """
    TODO
    scrapes the current price er kWH from the Bulb webpages tarrif, with selected options
    """
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver import Firefox
    import bs4
    import json

    # inputs
    pp_text = "By Direct Debit or other regular payment method"

    ff_opts = Options()
    ff_opts.add_argument("--headless")
    driver = webdriver.Firefox(options=ff_opts, executable_path="./geckodriver")

    # get page
    driver.get("https://bulb.co.uk/tariff/")

    # input postcode into website
    element = driver.find_element_by_xpath("//input[@id='postcode']")
    element.send_keys(post_code)
    print_html(element.get_attribute('innerHTML'))

    # choose payplan from table
    pay_plan = driver.find_element_by_xpath("//div[@aria-labelledby='paymentMethod-label']")
    print_html(pay_plan.get_attribute('innerHTML'))
    pay_plan.select_by_visible_text('pp_text')

############################################################

def create_empty_csv(field_names):
    """
    will create an empty csv with headers from inputted list
    """
    with open(name_of_csv, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        print(field_names)

############################################################

def append_to_csv(entry):
    """
    appends the data entry to a csv
    if it cant find csv it creates one
    """
    field_names = list(entry.keys())

    try:
        with open(name_of_csv, 'a') as f_object:
            dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(entry)
            print(list(entry.values()))
            f_object.close()

    except IOError:
        print("File not accessible/found")
        create_empty_csv(field_names)
        append_to_csv()

###########################################################

def get_live_price(ticker):
    """
    returns live ticker price from binance api in form of a dictionary
    with keys [symbol,price]
    """
    bin_api_url ="https://api.binance.com/api/v1/ticker/price?symbol={}".format(ticker)

    import requests
    import json
    response = json.loads(requests.get(bin_api_url).text)
    return response

############################################################