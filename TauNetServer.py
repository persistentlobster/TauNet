# Micah Burnett 11/30/15 CS300
# This is the server-side application for TauNet v1.0

import sys
import socket

HOST = ''           # local ip
PORT = 6283

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Socket creation failed, Error:", str(msg[0]), ", Msg:", msg[1])
    sys.exit()

print("Created socket")


try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print("Bind to socket failed:", str(msg[0]), ", Msg:", msg[1])

print("Bind successful")


sock.listen(5)
print("Listening for requests...")

#conn, addr = sock.accept()
#msg = conn.recv(1024)
#print(msg)

while True:
    conn, addr = sock.accept()
    msg = conn.recv(1024)
    print(msg)
    print ("Connected with " + addr[0] + ":" + str(addr[1]))

sock.close()


