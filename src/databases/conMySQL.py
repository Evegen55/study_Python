'''
Created on 25 мая 2016 г.

@author: Lartsev
'''
import mysql.connector

cnx = mysql.connector.connect(user='scott', password='tiger',
                              host='127.0.0.1',
                              database='employees')
cnx.close()