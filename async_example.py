import asyncio
import aiohttp
import time


async def fetch_page(session, url):
    start = time.time()
    async with session.get(url) as response:
        print(f'{url} took {time.time() - start}')
        return (url, response.status)


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


if __name__ == '__main__':

    def main():
        loop = asyncio.get_event_loop()
        urls = [
            'https://google.com',
            'https://google.com',
            'http://example.com',
            'https://www.youtube.com',
            'http://tecladocode.com/blog'
        ]
        start = time.time()
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        print(f'Total took {time.time() - start}')
        for page in pages:
            print(page)

    main()
