'''
Created on Nov 14, 2016

@author: Evgenii_Lartcev
'''
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
#host = socket.gethostbyaddr('192.168.0.103/24')
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done