"""Task6
Використовуючи сервіс https://jsonplaceholder.typicode.com/,
спробуйте побудувати різні типи запитів та обробити відповіді.
Необхідно попрактикуватися з urllib та бібліотекою requests.
Рекомендується спочатку спробувати виконати запити,
використовуючи urllib, а потім спробувати реалізувати те саме,
використовуючи requests.
"""

from urllib import request
from urllib.error import HTTPError, URLError
import json
from pprint import pprint

URL = "https://jsonplaceholder.typicode.com/posts"

# Get request
print('___Get___')

try:
    with request.urlopen(URL) as response:
        print('Content-Type:', response.getheader('Content-Type'))
        print(response.status)
        body = response.read()
except HTTPError as err:
    print(f'Status: {err.code}. "Reason: {err.reason}')
except URLError as err:
    print(err.reason)

posts = json.loads(body)
pprint(posts)

# Post request.
print('___Post___')

# data for new post
data = {"userId": 10,
        "title": "My POST REQUEST!",
        "body": "NEW POST from POST REQUEST!", }
data = str(data).encode('utf-8')

post_req = request.Request(URL, headers={}, data=data)
try:
    with request.urlopen(post_req) as response:
        print(response.status)
        pprint(response.read())
except HTTPError as err:
    print(f'Status: {err.code}. "Reason: {err.reason}')
except URLError as err:
    print(err.reason)

# Put request. Change/update 1st post
print('___Put___')

# new data for update
data = {"userId": 1,
        "title": "My Put REQUEST!",
        "body": "UPDATE POST by PUT REQUEST!", }
data = str(data).encode('utf-8')

put_req = request.Request(URL + '/1', headers={}, data=data, method='PUT')
try:
    with request.urlopen(put_req) as response:
        print(response.status)
        pprint(response.read())
except HTTPError as err:
    print(f'Status: {err.code}. "Reason: {err.reason}')
except URLError as err:
    print(err.reason)
