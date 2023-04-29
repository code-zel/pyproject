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

url = 'https://atlanta.craigslist.org/'
browser.get(url)


# click a hyperlink
for_sale_element = browser.find_element(By.XPATH, "/html/body/div[1]/section/div[3]/div[3]/div[2]/div/ul[1]/li[16]/a")
