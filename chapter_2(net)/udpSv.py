# 使用udp的服务端
import socket

HOST = ''
PORT = 12345
BUFFSIZE = 1024
ADDR = (HOST,PORT)

udpS = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpS.bind(ADDR)

while True:
    data, addr = udpS.recvfrom(BUFFSIZE)
    print('%s from %s' %(data.decode('utf-8'),addr))