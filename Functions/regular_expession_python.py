from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://nl.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,'html.parser')
    for link in bsObj.findAll(re.compile("[bewerken]")):
        print(link)
getLinks("/wiki/Python_(programmeertaal)")
