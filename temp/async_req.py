import time
import aiohttp
import asyncio


async def fetchPage(session, url):
    start = time.time()
    async with session.get(url) as res:
        print(f"page took {time.time() - start}")
        return res.status


async def multiplePages(loop, urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for u in urls:
            tasks.append(fetchPage(session, u))

        return await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()

urls = ['http://www.google.com' for i in range(10)]

start = time.time()

t = loop.run_until_complete(multiplePages(loop, urls))
print(t)
print(f"Program took {time.time() - start}")
