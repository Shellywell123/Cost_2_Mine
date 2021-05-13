import csv
import json
import requests
import statistics
from config import *
import _bulbql as bulbql


############################################################

def check_internet_connection():
    """
    """
    import urllib.request

    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
    except:
        return 'no internet'


############################################################


def print_html(html_str):
    """
    prints html code  with correct formating
    """
    from bs4 import BeautifulSoup

    print(BeautifulSoup(html_str, "html.parser").prettify())


############################################################


def get_live_kWhs_from_Bulb():
    """
    scrapes the current GBP per kWH from the Bulb webpages tarrif, with selected options
    """
    resp = makequery(tariff_options['post_code'], tariff_options['economy_7_meter'], tariff_options['pay_plan'])

    pence_per_kWH = float(parserates(resp))
    GBP_per_kWH = pence_per_kWH/100

    return GBP_per_kWH


############################################################


def makequery(postcode: str, eco7: bool, payplan: str) -> dict:
    """Makes a query against the Bulb GraphQL database

    :param payplan: One of `legacyPrepay`, `smartPayg`, `monthly`.

    :returns: Decoded JSON response of GraphQL
    """
    url = "https://join-gateway.bulb.co.uk/graphql"
    opname = "Tariffs"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "x-bulb-session": "15630c9a-577d-45da-a8ed",
        "content-type": "application/json",
        "Origin": "https://bulb.co.uk",
        "TE": "Trailers",
    }

    variables = {
        "postcode": postcode,
        "eco7": eco7,
        "legacyPrepay": False,
        "smartPayg": False,
        "monthly": True,
    }

    assert payplan in variables
    variables[payplan] = True

    query = dict(variables=variables, query=bulbql.mutation, operationName=opname)

    resp = requests.post(url, json=query, headers=headers)

    if 200 <= resp.status_code < 300:
        return resp.json()
    else:
        raise Exception("Bad Request.")


############################################################


def parserates(jsonresp: dict) -> float:
    """
    Extracts kWatt hour rates from json dictionary
    """
    
    rates = jsonresp["data"]["tariffs"]["residential"]["electricity"]["credit"]
    if "standard" in rates:
        # no day night average
        return rates["standard"][0]["unitRates"]["standard"]
    else:
        # average day and night
        unitRates = rates["economy7"][0]["unitRates"]
        return statistics.mean([unitRates["day"], unitRates["night"]])


############################################################


def create_empty_csv(name_of_csv):
    """
    will create an empty csv with headers from inputted list
    """
    with open(name_of_csv, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
    
    print('created {}'.format(name_of_csv))
    print(field_names)


############################################################


def append_to_csv(name_of_csv,entry):
    """
    appends the data entry to a csv
    if it cant find csv it creates one
    """
    field_names = list(entry.keys())

    import os
    if os.path.exists(name_of_csv):
        try: # incase file cant be written to as its beining viewwed
            with open(name_of_csv, "a") as f_object:
                dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
                dictwriter_object.writerow(entry)
                print(list(entry.values()))
                f_object.close()
        except:
            append_to_csv(entry)

    else:
        print("{} not found".format(name_of_csv))
        create_empty_csv(name_of_csv)
        append_to_csv(name_of_csv,entry)


###########################################################


def get_live_binance_spot_price(ticker):
    """
    returns live ticker price from binance api in form of a dictionary
    with keys [symbol,price]
    """
    bin_api_url = "https://api.binance.com/api/v1/ticker/price?symbol={}".format(ticker)

    response = requests.get(bin_api_url).json()
    return response


############################################################


def get_live_HiveOS_data():
    """
    returns live HiveOS farm info
    """
    HiveOS_login_api_url = "https://api2.hiveos.farm/api/v2/auth/login"

    # HiveOS Log in
    login_response = requests.post(
        HiveOS_login_api_url,
        data={"login": HiveOS_username, "password": HiveOS_password},
    ).json()
    auth_token = "Bearer " + access_token

    # HiveOS Farm info
    HiveOS_farm_api_url = "https://api2.hiveos.farm/api/v2/farms"
    farm_repsonse = requests.get(
        HiveOS_farm_api_url, data="", headers={"Authorization": auth_token}
    ).json()

    farm_data = farm_repsonse["data"][0]

    assert type(farm_data) == dict

    return farm_data


############################################################


def get_live_unMinable_data():
    """
    returns mining info of a unminable webpage from a address given in config.py
    """
        
    unmineable_api_url = "https://api.unminable.com/v3/stats/{}?tz=0&coin={}".format(doge_address,ticker_buy)
    response = (requests.get(unmineable_api_url).json())['data']
    return response


############################################################





