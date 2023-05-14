from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Using async and await to write concurrent code

import asyncio
import time
import random


async def save_to_db(content):
    """
    Simulates making a DB query to insert/update data
    """
    wait_time = random.randint(1, 2)
    await asyncio.sleep(wait_time)


async def get_content(url):
    """
    Simulates making an API call to fetch data
    """
    wait_time = random.randint(1, 5)
    await asyncio.sleep(wait_time)

    return [{
            "StockCode": "90129F",
            "Description": "RED GLASS TASSLE BAG CHARM",
            "UnitPrice": 2.95,
            "Quantity": 2,
            "TotalPrice": 5.9,
            "Country": "Japan",
            "InvoiceNo": "6dc735d6-ac5f-11ed-bdd3-d4619d3266c6",
            "Date": "2015/07/19"
           }, {
            "StockCode": "22457",
            "Description": "NATURAL SLATE HEART CHALKBOARD",
            "UnitPrice": 5.79,
            "Quantity": 3,
            "TotalPrice": 17.37,
            "Country": "Germany",
            "InvoiceNo": "6dc74058-ac5f-11ed-bdd3-d4619d3266c6",
            "Date": "2015/01/13"
           }, {
            "StockCode": "23471",
            "Description": "SIX DRAWER OFFICE TIDY",
            "UnitPrice": 9.95,
            "Quantity": 2,
            "TotalPrice": 19.9,
            "Country": "Germany",
            "InvoiceNo": "6dc743d2-ac5f-11ed-bdd3-d4619d3266c6",
            "Date": "2015/08/29"
            }]


async def extract_and_save(url):
    """
    Get response and save response to a DB
    """
    s1 = time.perf_counter()
    content = await get_content(url=url)
    await save_to_db(content=content)
    s2 = time.perf_counter()
    print(f'Extract and save for URL : {url}; Time elapsed: {s2 - s1:0.2f} seconds')


async def main():
    url1 = "https://jsonplaceholder.typicode.com/todos/{_id}".format(_id=1)
    url2 = "https://jsonplaceholder.typicode.com/todos/{_id}".format(_id=2)
    url3 = "https://jsonplaceholder.typicode.com/todos/{_id}".format(_id=3)

    await asyncio.gather(extract_and_save(url=url1), extract_and_save(url=url2), extract_and_save(url=url3))

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f'Total time elapsed: {t2-t1:0.2f} seconds')

# Write without async and await

import asyncio
import time
import random


def save_to_db(content):
    """
    Simulates making a DB query to insert/update data
    """
    wait_time = random.randint(1, 2)
    time.sleep(wait_time)


def get_content(url):
    """
    Simulates making an API call to fetch data
    """
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)

    return [{
            "StockCode": "90129F",
            "Description": "RED GLASS TASSLE BAG CHARM",
            "UnitPrice": 2.95,
            "Quantity": 2,
            "TotalPrice": 5.9,
            "Country": "Japan",
            "InvoiceNo": "6dc735d6-ac5f-11ed-bdd3-d4619d3266c6",
            "Date": "2015/07/19"
           }, {
            "StockCode": "22457",
            "Description": "NATURAL SLATE HEART CHALKBOARD",
            "UnitPrice": 5.79,
            "Quantity": 3,
            "TotalPrice": 17.37,
            "Country": "Germany",
            "InvoiceNo": "6dc74058-ac5f-11ed-bdd3-d4619d3266c6",
            "Date": "2015/01/13"
           }, {
            "StockCode": "23471",
            "Description": "SIX DRAWER OFFICE TIDY",
            "UnitPrice": 9.95,
            "Quantity": 2,
            "TotalPrice": 19.9,
            "Country": "Germany",
            "InvoiceNo": "6dc743d2-ac5f-11ed-bdd3-d4619d3266c6",
            "Date": "2015/08/29"
            }]


def extract_and_save(url):
    """
    Get response and save response to a DB
    """
    s1 = time.perf_counter()
    content = get_content(url=url)
    save_to_db(content=content)
    s2 = time.perf_counter()
    print(f'Extract and save for URL : {url}; Time elapsed: {s2 - s1:0.2f} seconds')


async def main():
    url1 = "https://jsonplaceholder.typicode.com/todos/{_id}".format(_id=1)
    url2 = "https://jsonplaceholder.typicode.com/todos/{_id}".format(_id=2)
    url3 = "https://jsonplaceholder.typicode.com/todos/{_id}".format(_id=3)

    extract_and_save(url=url1)
    extract_and_save(url=url2)
    extract_and_save(url=url3)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f'Total time elapsed: {t2-t1:0.2f} seconds')

# Simple ASGI application function

async def sample_app(receive, send):
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })
