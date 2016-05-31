'''
@author: Lartsev
'''
import urllib.request
import re
from bs4 import BeautifulSoup

hand = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_241994.html').read()
soup = BeautifulSoup(hand, 'html.parser')
a = 0
for p in soup.prettify().split(' '):
    if re.findall('[0-9]+', p):
        if p.rstrip().isnumeric():
            a = a+int(p)

print(a)