# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:48:24 2020

@author: Dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import urlopen
from bs4 import BeautifulSoup


url = input("Enter url: ")
html = urlopen(url)


soup = BeautifulSoup(html, 'lxml')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))