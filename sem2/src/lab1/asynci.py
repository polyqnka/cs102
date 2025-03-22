import asyncio

async def first_func():
    print('первый принт из first')
    await asyncio.sleep(1)
    print('это второоой принт из first')
    await asyncio.sleep(4)
    print('это третий принт из first')

async def second_func():
    print('this is first print from second_func')
    await asyncio.sleep(3)
    print('this is second print from second_func')
    await asyncio.sleep(1)
    print('this is third print from second_func')
    await asyncio.sleep(1)
    print('this is LAST print from second_func')

async def main():
    await asyncio.gather(first_func(), second_func())

asyncio.run(main())
