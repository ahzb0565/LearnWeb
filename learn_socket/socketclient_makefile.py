#!/usr/bin/evn python
'''
A simple sample of gopher client
Re-write by socket.makefile
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
    fd = s.makefile('wr', 0)
    fd.write('\r\n')
    for line in fd.readlines():
        sys.stdout.write(line)

if __name__ == '__main__':
    main()