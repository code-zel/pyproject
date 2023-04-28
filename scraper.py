import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://atlanta.craigslist.org/search/cta'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
}

query_string = 'honda'.replace(' ', '+')

posts = []

