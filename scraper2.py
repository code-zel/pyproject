from requests import get
from bs4 import BeautifulSoup
import time

search = "honda"
response = get('https://atlanta.craigslist.org/search/cta?query=honda#search=1~list~0~0')
time.sleep(5)

html_soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(5)

posts = html_soup.find_all('li', {'class' :'cl-search-result cl-search-view-mode-list'})

for post in posts:
    print(posts)
    print(len(posts))

html_soup.prettify()
