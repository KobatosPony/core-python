# 使用udp的客户端

import socket
import time

HOST = '127.0.0.1'
PORT = 12345
BUFFSIZE = 1024
ADDR = (HOST,PORT)

udpC = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    udpC.sendto('hello'.encode('utf-8'),ADDR)
    print('OK')
    time.sleep(1)