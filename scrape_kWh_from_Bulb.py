from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import bs4
import json

def print_html(html_str):
   """
   prints html code  with correct formating
   """
   from bs4 import BeautifulSoup
   print(BeautifulSoup(html_str, 'html.parser').prettify())

# inputs
post_code = "OL7 9LRx"
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
