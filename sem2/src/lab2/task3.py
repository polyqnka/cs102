import asyncio

async def delayed_message(delay: float, message: str) -> None:
    await asyncio.sleep(delay)
    print(message)

async def main():
    tasks = [
        delayed_message(2, "message after 2 seconds"),
        delayed_message(1, "message after 1 second"),
        delayed_message(3, "message after 3 seconds"),
    ]

    for task in asyncio.as_completed(tasks):
        await task

if __name__ == "__main__":
    asyncio.run(main())
