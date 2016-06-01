'''
@author: Lartsev

test it

Enter file name: http://python-data.dr-chuck.net/known_by_Nayeli.html
Enter position: 18
Enter number of steps: 7
Annika

'''
import urllib.request

from bs4 import BeautifulSoup

fname = input("Enter file name: ")
fpos  = input("Enter position: ")
fdeep = input("Enter number of steps: ")

def recursiveLinksName(filename1):
    hand = urllib.request.urlopen(filename1).read()
    soup = BeautifulSoup(hand, 'html.parser')
    tags = soup('a')
    l = []
    for tag in tags:
        l.append(tag.contents[0])
        #print ('Contents:',tag.contents[0])
    return l

def recursiveLinksURL(filename1):
    hand = urllib.request.urlopen(filename1).read()
    soup = BeautifulSoup(hand, 'html.parser')
    tags = soup('a')
    l = []
    for tag in tags:
        l.append(tag.get('href', None))
        #print ('URL:',tag.get('href', None))
    return l

def searchByURL(position, deep):
    i = 0
    a = 0
    name = ""
    l1 = recursiveLinksName(fname)
    l2 = recursiveLinksURL(fname)
    url_next = l2[position-1]

    while i < deep-1:
        l1 = recursiveLinksName(url_next)
        l2 = recursiveLinksURL(url_next)
        url_next = l2[position-1]
        name = l1[position-1]
        i = i + 1

    print(name)

searchByURL(int(fpos), int(fdeep))