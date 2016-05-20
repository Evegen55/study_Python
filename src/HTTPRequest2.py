'''
Created on 20 мая 2016 г.

@author: Lartsev
'''
import urllib.request
fhand = urllib.request.urlopen('https://wordpress.org/plugins/about/readme.txt')
for line in fhand:
    print(line.strip())
