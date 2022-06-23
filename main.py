
#%%
from soup_scrapers.soup_scrape import get_soup
from soup_parser.Google import Google_urls
from soup_parser.LinkedIn import LinkedIn_urls
from soup_parser.FaceBook import FaceBook_urls

search = 'Elissa Harika'
results = 200
google_url = "https://www.google.com/search?q={}&num={}".format(search, results)

google_soupe = get_soup(google_url)
extracted_urls = Google_urls(google_soupe,debug=True)
print('hi')
linkedin_urls = LinkedIn_urls(extracted_urls, debug=True)
facebook_urls = FaceBook_urls(extracted_urls)

# %%
