'''
Created on 23 мая 2016 г.

@author: Lartsev
'''
import urllib.request
from bs4 import BeautifulSoup
hand = urllib.request.urlopen('https://freelansim.ru/tasks').read()
soup = BeautifulSoup(hand, 'html.parser')
tags = soup('a')
for tag in tags:
    print (tag.get('href', None))
#print(soup.prettify())


