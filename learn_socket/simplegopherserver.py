#!/usr/bin/evn python
'''
A simple sample of gopher server
User telnet localhost 51423 to connect this socket
'''
import socket, sys

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))
s.listen(1)
print 'Press ctrl+c to terminate'

while 1:
    sckt, addr = s.accept()
    client_file = sckt.makefile('rw', 0)
    client_file.write("Welcome %s\n"%str(addr))
    client_file.write("Please enter a string:\n")
    line = client_file.readline().strip()
    client_file.write("You entered: %s\n"%line)
    client_file.close()
    sckt.close()