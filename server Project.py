# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:11:09 2020

@author: pateld23
"""

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 1234))
s.listen(1)   
print ('The server is ready for connection')                  

while True:
    clientSocket, address = s.accept()    
    print("Connection established with", address[0])
   
    clientMessage = clientSocket.recv(2048)
    print ('Client: ' + clientMessage.decode())
    
    fileName = 'hi.txt'

    try:
        f = open(fileName, 'rb')
    except (FileNotFoundError):
        print("FILE NOT FOUND!")
        clientSocket.close()
        sys.exit()
    
    f = open(fileName, 'rb')
    file = f.read(2048)
    
    while (file):
        clientSocket.send(file)
        print('File sent successfully!')
        file = f.read(2048)
    f.close()
    clientSocket.close()
    print('Connection closed')
    sys.exit()
    
