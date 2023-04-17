"""Task6
Використовуючи сервіс https://jsonplaceholder.typicode.com/,
спробуйте побудувати різні типи запитів та обробити відповіді.
Необхідно попрактикуватися з urllib та бібліотекою requests.
Рекомендується спочатку спробувати виконати запити,
використовуючи urllib, а потім спробувати реалізувати те саме,
використовуючи requests.
"""

import requests
from pprint import pprint

URL = "https://jsonplaceholder.typicode.com/posts"

# Get request. Get data
get_response = requests.get(URL)

if get_response:
    print("____Get Response____")
    pprint(get_response.text)
    print("____Status____")
    print(get_response.status_code)
else:
    print(get_response.status_code)
    print(get_response.reason)

# Post request. Create new post
# data for new post
data = {"userId": 10,
        "title": "My POST REQUEST!",
        "body": "NEW POST from POST REQUEST!", }


post_response = requests.post(URL, data=data)
# post_response = requests.post(WEBSITE, json=data)

if post_response:
    print("____Post Response____")
    pprint(post_response.text)
    print("____Status____")
    print(post_response.status_code)
else:
    print(post_response.status_code)
    print(post_response.reason)

# Put request. Change/update 1st post
# new data for update
data = {"userId": 1,
        "title": "My Put REQUEST!",
        "body": "UPDATE POST by PUT REQUEST!", }

# WEBSITE + '/1' - because we want to update post with id=1
put_response = requests.put(URL + '/1', data)

if post_response:
    print("____Put Response____")
    pprint(put_response.text)
    print("____Status____")
    print(put_response.status_code)
else:
    print(put_response.status_code)
    print(put_response.reason)

# Patch request. Change/update the part of 1st post
# new data for update
data = {"title": "My !PATCH! Request!", }
patch_response = requests.patch(URL + '/1', data)

if patch_response:
    print("____Patch Response____")
    pprint(patch_response.text)
    print("____Status____")
    print(patch_response.status_code)
else:
    print(put_response.status_code)
    print(put_response.reason)

# Delete request. Delete my post(id=101)
del_response = requests.delete(URL + '/101')
if del_response:
    print("____Del____")
    print(del_response)
else:
    print(del_response.status_code)
    print(del_response.reason)
