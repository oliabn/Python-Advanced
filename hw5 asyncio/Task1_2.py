"""Task1
Створіть співпрограму, яка отримує контент із зазначених посилань
і логує хід виконання в database, використовуючи стандартну
бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp.
Кроки, які мають бути залоговані: початок запиту до адреси X,
відповідь для адреси X отримано зі статусом 200. Перевірте хід
виконання програми на >3 ресурсах і перегляньте послідовність
запису логів в обох варіантах і порівняйте результати. Для двох
видів завдань використовуйте різні файли для логування, щоби
порівняти отриманий результат.
"""

import asyncio
import aiohttp
from Task1_1_db import create_db, path_to_db, insert_data_to_db_query, read_from_db

sites = ['https://jsonplaceholder.typicode.com/posts/1',
         'https://jsonplaceholder.typicode.com/posts/2',
         'https://jsonplaceholder.typicode.com/todos/3']


async def get_response_from_site(session, url):
    # print(f"Start of request for {url}")
    insert_data_to_db_query(f"Start of request for {url}")

    async with session.get(url) as response:
        # txt = await response.text()
        await response.text()
        # print(f"Response for {url} received with status {response.status}")
        insert_data_to_db_query(f"Response for {url} received with status {response.status}")


async def get_responses_from_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            # print(get_response_from_site(session, url))
            task = asyncio.ensure_future(get_response_from_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    # event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(get_responses_from_sites(sites))

    create_db(path_to_db)

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(get_responses_from_sites(sites))

    read_from_db()
