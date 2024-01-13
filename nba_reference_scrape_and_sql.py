# needed libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
# URL to scrape
url = "https://www.basketball-reference.com/playoffs/"

#%%
# collect HTML data
html = urlopen(url)      
# create beautiful soup object from HTML
soup = BeautifulSoup(html, features="lxml")
# use getText()to extract the headers into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]