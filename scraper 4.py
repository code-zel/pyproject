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

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
firefox_driver_path = os.path.join(os.getcwd(), 'geckodriver.exe')
firefox_service = Service(firefox_driver_path)
firefox_option = Options()
firefox_option.set_preference('general.useragent.override', user_agent)
browser = webdriver.Firefox(service=firefox_service, options=firefox_option)
browser.implicitly_wait(7)

url = 'https://atlanta.craigslist.org/search/cta'
browser.get(url)
time.sleep(3)


# click a hyperlink
searchbar = browser.find_element(By.XPATH, "/html/body/div[1]/main/form/div[1]/div/div/input")
searchbar.send_keys('honda')
time.sleep(5)
enter_button = browser.find_element(By.XPATH, "/html/body/div[1]/main/form/div[1]/button[1]")
enter_button.click()
time.sleep(3)

#store listings into csv
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

print(len(posts_html))

# now lets clean up our results

post = namedtuple('post', ['title', 'price', 'date', 'miles', 'location', 'post_url'])
posts = []

for post_html in posts_html:
    title = post_html.find('a', 'titlestring').text
    price = browser.find_element(By.CLASS_NAME, "priceinfo").get_attribute("textContent")
    date = post_html.find('div', 'meta').contents[0]
    miles = post_html.find('div', 'meta').contents[2]
    location = post_html.find('div', 'meta').contents[-1]
    post_url = post_html.find('a', 'titlestring').get('href')
    posts.append(post(title, price, date, miles, location, post_url))

print(posts[-5])



