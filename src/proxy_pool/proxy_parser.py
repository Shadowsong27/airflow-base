from bs4 import BeautifulSoup
from src.model import Proxy


def get_proxy_list():
    soup = BeautifulSoup(data, 'lxml')
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
