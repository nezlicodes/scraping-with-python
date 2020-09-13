# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:21:39 2020

@author: Dell
"""

from bs4 import BeautifulSoup
import requests as req

url = "https://boston.craigslist.org/search/sof"
res = req.get(url).text


soup = BeautifulSoup(res, 'html.parser')

tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))


titles = soup.find_all('a',{"class:", "result-title"})
print(titles[0])
