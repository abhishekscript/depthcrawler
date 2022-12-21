import sys

import requests
import validators
from bs4 import BeautifulSoup

from customlog import logger
from storage import storage_stack


def crawl(url: str, current_depth: int, depth: int):
    """Crawls given weburl untill current_depth reaches max allowed depth 

    Args:
        url (str): url to crawl
        current_depth (int): identifies current depth
        depth (int): the max depth allowed

    Yields:
        dict: keeps generating data with imageURL, sourceURL and depth
    """

    if current_depth >= depth:
        return

    print(f'Crawling {url} with current depth = {current_depth+1}')
    images, links = [], []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        images = soup.find_all('img')
    except Exception as e:
        logger.error(e)

    for image in images:
        src = image.get('src')
        storage_stack.push(
            {'imageURL': src, 'sourceURL': url, 'depth': current_depth + 1}
        )

    for link in links:
        next_url = link.get('href')
        crawl(next_url, current_depth+1, depth)


def command_line() -> dict:
    """Validates seed url and starts crawl process at certain depth."""

    arguments = sys.argv
    try:
        url = arguments[1]
        depth = int(arguments[2])
    except IndexError:
        print('Invalid Arguments')
        print(f'>> crawler.py <url> <depth>')
        return
    except ValueError:
        print('Depth must be an integer value')
        return

    if not validators.url(url):
        raise Exception('Invalid URL provided')

    data = []
    crawl(url, -1, depth)
    return {'results': data}


if __name__ == "__main__":
    command_line()
