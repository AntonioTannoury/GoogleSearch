def LinkedIn_urls(urls, debug = False):
    print('\nLinkedIN URLs')
    LinkedIn_urls = []
    if urls:
        for url in urls:
            if url:
                url = url.split("&")[0]
                if "linkedin.com" in url:
                    LinkedIn_urls.append(url)
                    if debug == True:
                        print('--'*20)
                        print(url)
    return LinkedIn_urls


def LinkedIn_info(soup):
    pass


#%%
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
email = 'webscrapersirenai@gmail.com'
password = 'webscraperwillflysoon'

# Creating an instance
driver = webdriver.Chrome(ChromeDriverManager().install())

# Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys(email)  # Enter Your Email Address

pword = driver.find_element_by_id("password")
pword.send_keys(password)        # Enter Your Password

driver.find_element_by_xpath("//button[@type='submit']").click()

# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://lb.linkedin.com/in/antonio-tannoury"

driver.get(profile_url)        # this will open the link

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000

    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed

    end = time.time()

    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break

src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

# In case of an error, try changing the tags used here.

name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces

works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()


location_loc = intro.find_all("span", {'class': 'text-body-small'})

# Ectracting the Location
# The 2nd element in the location_loc variable has the location
if location_loc:
    location = location_loc[1].get_text().strip()
else:
    location = ''
print("Name -->", name,
      "\nWorks At -->", works_at,
      "\nLocation -->", location)

# Getting the HTML of the Experience section in the profile
experience = soup.find("section", {"id": "experience-section"}).find('ul')

print(experience)

# In case of an error, try changing the tags used here.

li_tags = experience.find('div')
a_tags = li_tags.find("a")
job_title = a_tags.find("h3").get_text().strip()

print(job_title)

company_name = a_tags.find_all("p")[1].get_text().strip()
print(company_name)

joining_date = a_tags.find_all("h4")[0].find_all("span")[1].get_text().strip()

employment_duration = a_tags.find_all("h4")[1].find_all(
    "span")[1].get_text().strip()

print(joining_date + ", " + employment_duration)

# %%
