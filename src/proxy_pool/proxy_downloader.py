import requests
from src.constants import USER_AGENTS
import random


class ProxyDownloader:

    def __init__(self, proxy_enabled=False):
        self.targets = [
            "https://free-proxy-list.net/"
        ]

    def get_page_source(self, url):
        headers = {
            'user-agent': self.get_random_user_agent()
        }
        r = requests.get(url, headers=headers)
        return url, r.content

    @staticmethod
    def get_random_user_agent():
        return random.choice(USER_AGENTS)

    def execute(self):
        for target in self.targets:
            self.get_page_source(target)


if __name__ == '__main__':
    d = ProxyDownloader()
    d.execute()
