import csv
import json
import requests
import statistics
from config import *
import _bulbql as bulbql

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


def create_empty_csv(field_names):
    """
    will create an empty csv with headers from inputted list
    """
    with open(name_of_csv, "w") as csvfile:
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
        with open(name_of_csv, "a") as f_object:
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

    return farm_data


############################################################


def get_live_unMinable_data():
    """
    returns mining info of a unminable webpage from a address given in config.py
    """
    try:
        
        unmineable_url = "https://unmineable.com/coins/DOGE/address/{}".format(doge_address)
        response = requests.get(unmineable_url).text

        from requests_html import HTMLSession
        from bs4 import BeautifulSoup

        # create an HTML Session object
        session = HTMLSession()

        # Use the object above to connect to needed webpage
        resp = session.get(unmineable_url)

        # Run JavaScript code on webpage
        resp.html.render(sleep=2, keep_page=True,timeout=20)

        # print(resp.html.html)

        soup = BeautifulSoup(resp.html.html, "lxml")

        to_be_paidout = (
            str(soup.find_all(id="pending_mining_balance"))
            .split('id="pending_mining_balance">')[1]
            .split("<")[0]
        )

        mined_24 = str(soup.find_all(id="total_24h")).split('aria-label="')[1].split('"')[0]
        total_paidout = (
            str(soup.find_all(id="total_paid")).split('aria-label="')[1].split('"')[0]
        )
        last_payout_date = (
            str(soup.find_all(id="last_payment_date"))
            .split('class="number-important">')[1]
            .replace("</b><span>", " ")
            .split("</span>")[0]
        )
        payout_fee = (
            str(soup.find_all(id="current-fee")).split('id="current-fee">')[1].split("<")[0]
        )
        amount_for_auto_payout = (
            str(soup.find_all(id="threshold_amount"))
            .split('id="threshold_amount">')[1]
            .split("<")[0]
        )
        is_auto_payout_checked = str(soup.find_all(id="setting-auto_pay")).split('"')[1]

        session.close()

        unMineable_data = {
            "to_be_paidout": to_be_paidout,
            "mined in last 24hrs": mined_24,
            "total_paidout": total_paidout,
            "last_payout_date": last_payout_date,
            "payout_fee": payout_fee,
            "is_auto_payout_checked": is_auto_payout_checked,
            "amount_for_auto_payout": amount_for_auto_payout,
        }

        return unMineable_data

    except:

        get_live_unMinable_data()

############################################################
