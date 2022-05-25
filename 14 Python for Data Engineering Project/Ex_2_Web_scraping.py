from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd
from urllib.request import urlopen

web_link = "https://en.wikipedia.org/wiki/List_of_largest_banks"
page = urlopen(web_link)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
print(type(soup))
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])