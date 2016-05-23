'''
Created on 20 мая 2016 г.

@author: Lartsev
'''
import re
fo = open("regex_sum_241989.txt")
a = 0
for line in fo:
    line = line.rstrip()
    if re.findall('[0-9]+', line):
        res = re.split(' ', line)
        for s in res:
            if re.findall('[0-9]+', s):
                a = a+int(s)
                #print(a)
print(a)
