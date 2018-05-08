from socket import *

HOST = '10.1.0.21'
PORT = 7878
BUFFSIZE = 4096
ADDR = (HOST,PORT)

udpCli = socket(AF_INET,SOCK_DGRAM)
udpCli.bind(ADDR)

while True:
    data,addr = udpCli.recvfrom(BUFFSIZE)
    print('Get msg %s from %s' %(data.decode('utf-8'),str(addr)))