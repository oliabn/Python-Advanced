"""Task8
Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу
та словник як передавальні дані (опціональний).
Виконувати запит з отриманим методом на отриманий ресурс, передаючи
дані відповідним методом, та друкувати на консоль статус-код,
заголовки та тіло відповіді.
"""

import requests
from requests.exceptions import HTTPError
from pprint import pprint


def get(url):
    """Do Get Request and return a response"""
    try:
        response = requests.get(url)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('\nGet request:')
        if response:
            print('Status code:', response.status_code)
            print('\nBody:')
            pprint(response.text)
            print('\nHeaders')
            pprint(response.headers)
        else:
            print(response.status_code)
            print(response.reason)


def post(url, data):
    """Do Post Request and return a response"""
    try:
        response = requests.post(url, data=data)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('\nPost request:')
        if response:
            print('Status code:', response.status_code)
            print('\nBody:')
            pprint(response.text)
            print('\nHeaders')
            pprint(response.headers)
        else:
            print(response.status_code)
            print(response.reason)


def put(url, data):
    """Do Put Request and return a response"""
    try:
        response = requests.put(url, data=data)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('\nPut request:')
        if response:
            print('Status code:', response.status_code)
            print('\nBody:')
            pprint(response.text)
            print('\nHeaders')
            pprint(response.headers)
        else:
            print(response.status_code)
            print(response.reason)


def delete(url):
    """Do Delete Request and return a response"""
    try:
        response = requests.delete(url)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('\nDelete request:')
        if response:
            print('Status code:', response.status_code)
        else:
            print(response.status_code)
            print(response.reason)


def http_client(url, method='get', data={}):
    match method:
        case 'get':
            get(url)
        case 'post':
            post(url, data)
        case 'put':
            put(url, data)
        case 'del' | 'delete':
            return delete(url)
        case _:
            print('Incorrect method. Use get, put delete or del')


# Test
if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/posts"

    # get
    http_client(url)

    # put
    data = {"userId": 1,
            "title": "My Put REQUEST!",
            "body": "UPDATE POST by PUT REQUEST!", }
    http_client(url + '/1', method='put', data=data)

    # post
    # data for new post
    data = {"userId": 10,
            "title": "My POST REQUEST!",
            "body": "NEW POST from POST REQUEST!", }
    http_client(url, method='post', data=data)

    # delete
    http_client(url + '/101', method='del')
