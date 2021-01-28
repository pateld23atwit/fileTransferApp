# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:13:26 2020

@author: pateld23
"""

import socket                  
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
print("Connected to", socket.gethostbyname(socket.gethostname()))

s.send(("Requesting file").encode())
f = input('Enter name for incoming file: ')

file_data = s.recv(2048)
file = open(f, 'wb')
file.write(file_data)

file.close()

emptyFile = os.path.getsize(f)

if emptyFile == 0:
    print ("NO FILE RECIEVED OR FILE IS EMPTY!")
    file.close()
    os.remove(f)
    s.close()
    sys.exit()
    
print('connection closed')    
print('File recieved')

s.close()
print('connection closed')
sys.exit()