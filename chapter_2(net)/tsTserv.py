# 创建tcp时间戳服务器

from socket import *
from time import ctime

HOST = ''
PORT = 12345
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)

# 表示同时最多五个client访问
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:' + str(addr))

    while True:
        data = tcpCliSock.recv(BUFFSIZE).decode('utf-8')
        if not data:
            break

        print('recv: %s' %data)
        tcpCliSock.send('[%b] %b'.encode('utf-8') %(ctime().encode('utf-8'),data.encode('utf-8')))
    tcpCliSock.close()