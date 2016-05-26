'''
Created on 26 мая 2016 г.

@author: Lartsev
'''
import sqlite3

con = sqlite3.connect('DatabaseName1.db')

curr = con.cursor()
curr.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

