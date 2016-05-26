'''
Created on 19 мая 2016 г.

@author: Lartsev
'''
import re


fo = open("mbox-short.txt")

for line in fo:
    line = line.rstrip()
    if re.search('^F.+?: ', line):
        print(line)   
