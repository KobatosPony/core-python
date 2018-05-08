# 创建tcp时间戳客户端

from socket import *

HOST = '127.0.0.1'
PORT = 12345
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)

# 尝试连接到服务器
tcpCliSock.connect(ADDR)

while True:
    data = input('>>')
    data = data.encode('utf-8')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()