
import csv

def print_html(html_str):
   """
   prints html code  with correct formating
   """
   from bs4 import BeautifulSoup
   print(BeautifulSoup(html_str, 'html.parser').prettify())


def scrape_kWhs_from_Bulb():
    """
    """
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver import Firefox
    import bs4
    import json

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

def create_empty_csv(field_names):
    """
    """
    with open('Mining_Balance_Sheet.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

def append_to_csv(entry):
    """
    """
    field_names = list(entry.keys())

    try:
        f = open("Mining_Balance_Sheet.csv")
        # Do something with the file

        # Open your CSV file in append mode
        # Create a file object for this file
        with open('Mining_Balance_Sheet.csv', 'a') as f_object:
              
            # Pass the file object and a list 
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
          
            #Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(entry)
          
            #Close the file object
            f_object.close()

    except IOError:
        print("File not accessible")
        create_empty_csv(field_names)
        append_to_csv()

    finally:
        f.close()
