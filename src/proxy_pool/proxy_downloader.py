import requests
from src.constants import USER_AGENTS
import random
from bs4 import BeautifulSoup
from src.model import Proxy
import logging


class ProxyDownloader:

    def __init__(self, proxy_enabled=False):
        pass

    def get_page_source(self, url):
        headers = {
            'user-agent': self._get_random_user_agent()
        }
        r = requests.get(url, headers=headers)
        return r.content

    @staticmethod
    def _get_random_user_agent():
        return random.choice(USER_AGENTS)


class ProxyParser:

    def parse(self, domain_string, page_source):
        parser = self._get_parser(domain_string)
        return parser(page_source)

    def _get_parser(self, domain_string):
        if domain_string == "https://free-proxy-list.net/":
            return self._free_proxy_list

    @staticmethod
    def _free_proxy_list(page_source):
        soup = BeautifulSoup(page_source, 'lxml')
        result = []
        trs = soup.find_all('tr')
        for tr in trs[1:]:

            try:
                tds = tr.find_all('td')
                address = tds[0].text
                port = tds[1].text
                is_https = tds[5].text

                result.append(Proxy(address, port, is_https))
            except IndexError:
                break

        return result


class ProxyPoolController:

    def __init__(self):
        self.downloader = ProxyDownloader()
        self.parser = ProxyParser()

        self.sources = [
            "https://free-proxy-list.net/"
        ]

    def fetch_proxies(self):
        for source in self.sources:
            logging.info("Fetching proxies from domain: {}".format(source))
            page_source = self.downloader.get_page_source(source)
            proxies = self.parser.parse(source, page_source)
            print(proxies)

    def check_proxy_status(self):
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    c = ProxyPoolController()
    c.fetch_proxies()
