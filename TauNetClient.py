# Micah Burnett 11/30/15 CS303
# Client Application for TauNet v1.0

import sys
import socket


#connect to local host. TODO: change...
HOST = '192.168.0.2'   
PORT = 6283

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srvAddr = socket.gethostbyname(HOST)
sock.connect((srvAddr, PORT))     
sock.send("Yo dawg")

"""while True:
    print("Establishing connection to server...")
    conn, addr = sock.accept()

    
    msg = conn.recv(1024)
    print("Received msg:", msg)

    conn.close()"""
