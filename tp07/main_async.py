import asyncio
import time

async def add(a,b):
    await asyncio.sleep(0.5)
    return a+b

async def main():
    start = time.perf_counter()
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # c = await add(1,2)
    # print(c)
    # c = await add(1,3)
    # print(c)
    # c = await add(1,4)
    # print(c)
    r = [add(1,2),add(1,3),add(1,4)]

    all = await asyncio.gather(*r)
    print(all)

    end = time.perf_counter()
    print(end-start)
if __name__=='__main__':
    asyncio.run(main())
