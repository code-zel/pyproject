import os
import time
import datetime
from collections import namedtuple
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
import pandas as pd

#user input for what car they would like to search for
car = input("What type of car are you looking for?")

#info needed for selenium 

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
firefox_driver_path = os.path.join(os.getcwd(), 'geckodriver.exe')
firefox_service = Service(firefox_driver_path)
firefox_option = Options()
firefox_option.set_preference('general.useragent.override', user_agent)
browser = webdriver.Firefox(service=firefox_service, options=firefox_option)
browser.implicitly_wait(7)

#opening the browser to desired page 
url = 'https://atlanta.craigslist.org/search/cta'
browser.get(url)
time.sleep(3)


# click a hyperlink
searchbar = browser.find_element(By.XPATH, "/html/body/div[1]/main/form/div[1]/div/div/input")
searchbar.send_keys(car)
time.sleep(5)
enter_button = browser.find_element(By.XPATH, "/html/body/div[1]/main/form/div[1]/button[1]")
enter_button.click()
time.sleep(3)

#creating the list of results, querying first 4 pages of listings
posts_html = []
x=0
while x<4:
    search_results = browser.find_element(By.ID, "search-results-page-1")
    soup = BeautifulSoup(search_results.get_attribute('innerHTML'), 'html.parser')
    posts_html.extend(soup.find_all('li', {'class': 'cl-search-view-mode-gallery'}))
    button_next = browser.find_element(By.CLASS_NAME, "cl-next-page")
    button_next.click()
    time.sleep(1.5)
    x=x+1

# test line used to make sure we are populating the list: print(len(posts_html))

# now lets clean up our results into attributes

post = namedtuple('post', ['title', 'price', 'date', 'miles', 'location', 'post_url'])
posts = []

for post_html in posts_html:
    title = post_html.find('a', 'titlestring').text
    price = post_html.find('div', 'gallery-card').contents[3].text
    date = post_html.find('div', 'meta').contents[0]
    miles = post_html.find('div', 'meta').contents[2]
    location = post_html.find('div', 'meta').contents[-1]
    post_url = post_html.find('a', 'titlestring').get('href')
    posts.append(post(title, price, date, miles, location, post_url))

# test line print(posts[-5])

#create csv file

df = pd.DataFrame(posts)
df.to_csv(f'results ({datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S")}).csv', index=False)

browser.close()



