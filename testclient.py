'''
Test Client

@author: bobzhou
'''

import socket
import sys
import traceback

size = 10
dir = 1
pos = 0

def spin():
    global size, dir,pos
    string = '.'*pos + "|"+'.'*(size - pos - 1)
    sys.stdout.write("\r" + string+" ")
    sys.stdout.flush()

    pos += dir
    if pos < 0:
        dir = 1
        pos = 1
    elif pos >= size:
        pos -=2
        dir = -1

if __name__ == '__main__':
    host = ''
    port = 51423

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except:
        traceback.print_exc()
        sys.exit()
    while 1:
        try:
            data = s.recv(1024)
            if not len(data):
                break
            sys.stdout.write("\r"+data)
            sys.stdout.flush()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            sys.exit()
        spin()