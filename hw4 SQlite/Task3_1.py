""""Task3
Змініть таблицю так, щоби можна було додати
не лише витрати, а й прибутки.
"""

"""Task3_1 Create profits table"""

from Task1 import create_connection, execute_query

path_to_profits = './data/profits.sqlite3'

create_profits_table_query = """
   CREATE TABLE IF NOT EXISTS profits (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   source TEXT NOT NULL,
   amount REAL NOT NULL,
   time timestamp);
   """

if __name__ == '__main__':
    # create DB 'profits'
    db = create_connection(path_to_profits)
    execute_query(db, create_profits_table_query)    # create table

    if db:
        db.close()
