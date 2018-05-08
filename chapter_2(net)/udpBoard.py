from socket import *
import time

# udp 的广播发送
HOST = '<broadcast>'
PORT = 7878
BUFFSIZE = 4096
ADDR = (HOST,PORT)

udpSock = socket(AF_INET,SOCK_DGRAM)
udpSock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    udpSock.sendto('A broadcast message!'.encode('utf-8'),ADDR)
    print('success to send a msg')
    time.sleep(2)