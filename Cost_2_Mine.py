import csv
from config import *
import requests

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
    TODO - requires selenium
    scrapes the current price er kWH from the Bulb webpages tarrif, with selected options
    """
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver import Firefox

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

    response = requests.get(bin_api_url).json()
    return response

############################################################

def get_live_HiveOS_data():
    """
    returns live HiveOS farm info
    """
    HiveOS_login_api_url = 'https://api2.hiveos.farm/api/v2/auth/login'

    # HiveOS Log in
    login_response = requests.post(HiveOS_login_api_url, data = {"login": HiveOS_username,  "password": HiveOS_password}).json()
    auth_token = "Bearer " + access_token

    # HiveOS Farm info
    HiveOS_farm_api_url = 'https://api2.hiveos.farm/api/v2/farms'
    farm_repsonse = requests.get(HiveOS_farm_api_url, data = "", headers = {"Authorization": auth_token}).json()

    farm_data = farm_repsonse['data'][0]
    
    return farm_data

############################################################

def get_live_unMinable_data():
    """
    returns mining info of a unminable webpage from a address given in config.py
    """
    unmineable_url = "https://unmineable.com/coins/DOGE/address/{}".format(doge_address)
    response = requests.get(unmineable_url).text

    from requests_html import HTMLSession
    from bs4 import BeautifulSoup
     
    # create an HTML Session object
    session = HTMLSession()
     
    # Use the object above to connect to needed webpage
    resp = session.get(unmineable_url)
     
    # Run JavaScript code on webpage
    resp.html.render(sleep=1, keep_page=True)

    #print(resp.html.html)

    soup = BeautifulSoup(resp.html.html, "lxml")

    mined_til_payout       = str(soup.find_all(id='pending_mining_balance')).split('id="pending_mining_balance">')[1].split('<')[0]
    mined_24               = str(soup.find_all(id='total_24h')).split('aria-label="')[1].split('"')[0]
    total_paidout          = str(soup.find_all(id='total_paid')).split('aria-label="')[1].split('"')[0]
    last_payout_date       = str(soup.find_all(id='last_payment_date')).split('class="number-important">')[1].replace('</b><span>',' ').split('</span>')[0]
    payout_fee             = str(soup.find_all(id='current-fee')).split('id="current-fee">')[1].split('<')[0]
    amount_for_auto_payout = str(soup.find_all(id='threshold_amount')).split('id="threshold_amount">')[1].split('<')[0]
    is_auto_payout_checked = str(soup.find_all(id='setting-auto_pay')).split('"')[1]

    unMineable_data={
        'mined_til_payout'       : mined_til_payout,
        'mined in last 24hrs'    : mined_24,
        'total_paidout'          : total_paidout,
        'last_payout_date'       : last_payout_date,
        'payout_fee'             : payout_fee,
        'is_auto_payout_checked' : is_auto_payout_checked
    }

    return unMineable_data

############################################################
