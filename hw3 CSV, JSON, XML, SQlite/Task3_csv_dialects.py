"""Task3
Попрацюйте зі створенням власних діалекті.
Зарееструйте власні діалекти та
записуйте/читайте файли з ними.
"""

import csv


class CustomDialect(csv.Dialect):
    """My custom dialect"""
    quoting = csv.QUOTE_MINIMAL     # It defaults to QUOTE_MINIMAL
    quotechar = " "                 # to quote fields containing special characters. It defaults to '"'
    delimiter = "*"                 # to separate fields. It defaults to ','
    lineterminator = '\n'           # to terminate lines produced by the writer. It defaults to '\r\n'


csv.register_dialect('custom_dialect', CustomDialect)

# write data with custom_dialect to file
with open('data/task3.csv', 'w') as file:
    writer = csv.writer(file, dialect='custom_dialect')
    writer.writerow(['1', '2', '3'])
    writer.writerow(['4', '5', '6'])

# read data with custom_dialect from file
with open('data/task3.csv', 'r') as file:
    reader = csv.reader(file, dialect='custom_dialect')
    for row in reader:
        print(row)
