#!/usr/bin/env python
#Simple Gopher Client

import socket, sys

def main():
    port = 70
    host = 'quux.org'
    #host = 'www.example.com'
    filename = '/'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print "Error connecting %s"%host
        print "Error code: %s"%str(e)
        sys.exit(1)
    s.sendall(filename + "\r\n")

    while 1:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)

if __name__ == "__main__":
    main()