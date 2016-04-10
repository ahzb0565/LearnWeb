'''
Created on Mar 11, 2016

@author: bobzhou
'''
import socket

if __name__ == '__main__':
    host = 'www.baidu.com'
    results = socket.getaddrinfo(host, None)
    for item in results:
        print item