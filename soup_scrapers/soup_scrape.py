import random
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    port = random.randint(1111, 9999)
    page = requests.get(url, proxies={"http": "http://111.233.225:{}".format(port)})
    return BeautifulSoup(page.content, "html5lib")
