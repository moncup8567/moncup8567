#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5007
BUFFER_SIZE = 1024
MESSAGE = input("Input your number: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str(MESSAGE))
data = s.recv(BUFFER_SIZE)
s.close()
print "send number:", MESSAGE
print "answer from server:", data
