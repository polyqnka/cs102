import asyncio

async def delayed_message(delay: float, message: str) -> None:
    await asyncio.sleep(delay)
    print(message)


import time

async def main():
    start = time.time()
    await delayed_message(2, "привет через 2 секунды")
    print(f"Прошло времени: {time.time() - start:.2f} сек.")

asyncio.run(main())
