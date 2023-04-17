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

"""Task5_3 - Main"""

from Task5_1 import get_data_for_table_from_monobank
from Task5_2 import create_exchange_table, insert_data_to_db_query, read_from_db

currency_data = get_data_for_table_from_monobank()
create_exchange_table()
insert_data_to_db_query(currency_data)

# Test: Checking what is now in the table
read_from_db()
