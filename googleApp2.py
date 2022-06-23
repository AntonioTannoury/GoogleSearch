#%%
import requests
from bs4 import BeautifulSoup
import re
# import requests
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry


# # session = requests.Session()
# # retry = Retry(connect=3, backoff_factor=0.5)
# # adapter = HTTPAdapter(max_retries=retry)
# # session.mount('http://', adapter)
# # session.mount('https://', adapter)

# # session.get(url)


search = "Antonio Tannoury"
results = 1
page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results),proxies={"http": "http://111.233.225.166:1235"})
soup = BeautifulSoup(page.content, "html5lib")

re_url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' 

for tag in soup.find_all(re.compile("^a"), href=True):
    href = tag['href']
    url = re.findall(re_url, href)
    print(url)
    # if url:
    #     url = url[0].split('&')[0]

    #     if 'linkedin.com/in/' in url:
    #         print('--'*20)
    #         print(url)
        
    #     elif 'www.facebook.com/' in url:
    #         print('--'*20)
    #         print(url)

# %%
