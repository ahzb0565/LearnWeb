#!/usr/bin/evn python
'''
A simple sample of gopher client
'''

import socket, sys

port = 70
host = 'quux.org'
filename = '/'

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print str(e)
        sys.exit(1)
    s.sendall(filename + '\r\n')
    while 1:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)

main()