import asyncio
import aiohttp
import async_timeout
import requests
import logging
import time

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger('scraping')

loop = asyncio.get_event_loop()

print('Loading books list...')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.debug('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

_books = []


async def fetch_page(session, url):
    logger.info(f'Requesting {url}')
    async with async_timeout.timeout(15):
        start = time.time()
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


logger.info(f'Going through {page.page_count} pages of books...')

# other URLs to try:
# https://www.johnlewis.com/herman-miller-new-aeron-office-chair-graphite-polished-aluminium/p3177260
# http://google.com
urls = [
    f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests took {time.time() - start}')

for page_content in pages:

    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    _books.extend(page.books)

books = _books
print(len(books), books)
