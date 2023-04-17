"""Task5
Create an Exchange Rates To USD db using API Monobank (api.monobank.ua).
Do requests via request lib, parse results, write it into db.
(3 examples required)
Example:
Table - Exchange Rate To USD:

id (INT PRIMARY KEY) - 1, 2, 3, ...
currency_name (TEXT) - UAH
currency_value (REAL) - 39.5
current_date (DATETIME) - 10/22/2022 7:00 PM
"""

"""Task5_1 - Functions for getting currency data from monobank"""

import requests
from iso4217 import find_currency
from requests.exceptions import HTTPError
import datetime

URL = 'https://api.monobank.ua/bank/currency'


def get_currency_data_from_mono(url: str) -> list:
    """Get data from monobank"""

    try:
        response = requests.get(url)
        currency_data_from_mono = response.json()
        # print(currency_data_from_mono)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        # print('Success!')
        return currency_data_from_mono


def get_currencies_for_db(data_from_mono: list):
    """Forming a list of tuples with currency data.
    Tuples in the list that are suitable for writing to the database.
    Since the Monoband provides information about the value of the
    currency in dollars only about the hryvnia, a list with one
    tuple is issued"""

    currencies = []
    for data in data_from_mono:
        if data['currencyCodeA'] == 840 and data['rateBuy'] != 0:
            currencies.append(
                (find_currency(numeric_code=data['currencyCodeB']).currency_name,
                              data['rateBuy'],
                              datetime.datetime.now())
                )
    # print(currencies)
    return currencies


def get_data_for_table_from_monobank():
    """Return list of tuples for insert it to table"""

    currency_data = get_currencies_for_db(get_currency_data_from_mono(URL))
    return currency_data


if __name__ == "__main__":
    for valuta in get_data_for_table_from_monobank():
        print(valuta)
