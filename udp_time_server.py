#!/usr/bin/env python
#Udp time server

import socket, struct, traceback, time

host = ''#bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while 1:
    try:
        msg, addr = s.recvfrom(8192)
        secs = int(time.time())
        reply = struct.pack(secs)
        s.sendto(reply, addr)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
