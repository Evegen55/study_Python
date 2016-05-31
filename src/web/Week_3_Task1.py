'''
Created on 20 мая 2016 г.

@author: Lartsev
'''
import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
#see http://stackoverflow.com/questions/5471158/typeerror-str-does-not-support-the-buffer-interface
#mysock.send(bytes('GET http://www.py4inf.com/code/demo/romeo.txt HTTP/1.0\n\n', 'UTF-8'))
#mysock.send(bytes('GET http://www.dailytechinfo.org/infotech/8120-kompaniya-google-razrabotala-sobstvennyy-specializirovannyy-processor-prednaznachennyy-dlya-sistem-iskusstvennogo-intellekta.html HTTP/1.0\n\n', 'UTF-8'))
mysock.send(bytes('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n', 'UTF-8'))

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data)
mysock.close()