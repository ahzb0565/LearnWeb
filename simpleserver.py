#!/usr/bin/env python
#Simple Gopher Server

import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Server is running on port %d, press CTRL+C to exit"%port

while 1:
    clientsocket, clientaddr = s.accept()
    clientfile = clientsocket.makefile("rw", 0)
    clientfile.write("Welcome to bob\'s %s server."%str(clientaddr))
    clientfile.write("PLS enter a string:")
    line = clientfile.readline().strip()
    clientfile.write("You enterd: %s"%line)
    clientfile.close()
    clientsocket.close()