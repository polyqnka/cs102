import requests
import time
import aiohttp
import asyncio

urls = [
    "https://httpstat.us/200?sleep=3000",
    "https://httpstat.us/200?sleep=1000",
    "https://httpstat.us/200?sleep=2000",
]

# синхронный запрос

def sync_requests(urls):
    print("Синхронный запрос:")
    start = time.time()
    for url in urls:
        t0 = time.time()
        response = requests.get(url)
        elapsed = time.time() - t0
        print(f"{url} → статус: {response.status_code}, время: {elapsed:.2f} сек.")
    print(f"Общее время: {time.time() - start:.2f} сек.\n")

# асинхронный запрос

async def fetch(session, url):
    t0 = time.time()
    async with session.get(url, ssl=False) as response:  # ssl=False временно
        await response.text()
        elapsed = time.time() - t0
        print(f"{url} → статус: {response.status}, время: {elapsed:.2f} сек.")

async def async_requests(urls):
    print("Асинхронный запрос:")
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)
    print(f"Общее время: {time.time() - start:.2f} сек.\n")


if __name__ == "__main__":
    sync_requests(urls)
    asyncio.run(async_requests(urls))
