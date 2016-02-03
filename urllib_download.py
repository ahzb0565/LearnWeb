#!/usr/bin/env python

#Use urllib to download files from socket

import urllib, sys

def sample1():
    host = sys.argv[1]
    file = sys.argv[2]
    f = urllib.urlopen("gopher://%s%s"%(host, file))
    for l in f.readlines():
        sys.stdout.write(l)

def semple2():
    f = urllib.urlopen(sys.argv[1])
    while 1:
        buf = f.read(2048)
        if not buf:
            break
        sys.stdout.write(buf)