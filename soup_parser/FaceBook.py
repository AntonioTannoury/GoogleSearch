from math import degrees
import random
import requests
from bs4 import BeautifulSoup


def FaceBook_urls(urls, debug = False):
    print("\nFacebook URLs")

    FaceBook_urls = []
    if urls:
        for url in urls:
            if url:
                url = url.split('&')[0]
                if 'www.facebook.com/' in url:
                    FaceBook_urls.append(url)
                    if debug == True:
                        print('--'*20)
                        print(url)
    return FaceBook_urls

def FaceBook_info(soup):
    pass