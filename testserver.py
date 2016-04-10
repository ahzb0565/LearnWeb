'''
Test server

@author: bobzhou
'''
import socket
import traceback
import time

if __name__ == '__main__':
    host = ''
    port = 51423

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(1)
    print "Server started..."
    while 1:
        try:
            clnt_s,addr = s.accept()
            print "Connect from %s"%str(addr)
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue

        try:
            while 1:
                try:
                    clnt_s.sendall(time.asctime() + '\n')
                except:
                    traceback.print_exc()
                    break
                time.sleep(2)
        except:
            traceback.print_exc()
        try:
            clnt_s.close()
        except:
            traceback.print_exc()