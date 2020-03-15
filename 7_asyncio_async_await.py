# план
# 1 async фреймворк для создания событийных циклов
# 2 пример простой асинхронной программы python 3.4
# 3 пример асинхронного скачивания файлов

# event-loop
# coroutine > Task > (Future)

import asyncio
from time import time

# @asyncio.coroutine
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1) #yield from


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task((print_nums()))
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop.close()
    asyncio.run(main())

