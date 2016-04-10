'''
Get port by local avail ports and DNS
'''
import socket
import logging
import sys
logging.basicConfig(level = logging.DEBUG)

dns = 'www.baidu.com'

if __name__ == '__main__':
    logging.debug("Creating socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.debug('Lookup for ports')
    port = socket.getservbyname('http')
    logging.debug('Connecting host on port %d'%port)
    try:
        s.connect((dns, port))
    except socket.gaierror, e:
        print str(e)
        sys.exit()
    logging.debug('Connected from: %s'%str(s.getsockname()))
    logging.debug('Connected to: %s'%str(s.getpeername()))