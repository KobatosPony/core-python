# 使用 socketserver 创建TCP客户端

from socket import *

HOST = 'localhost'
PORT = 12345
BUFFSIZE = 1024
ADDR = (HOST,PORT)

while True:
    # 因为socketserver的服务器每次都会默认关闭连接
    # 所以不能保持连接而要每次都创建一个新的套接字
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    data = input('>>')
    if not data:
        break
    # 由于StreamRequestHandler通信类似于文件
    # 所以必须发送行终止符（回车和换行符）
    tcpCliSock.send('%s\r\n'.encode('utf-8') % data.encode('utf-8'))
    r_data = tcpCliSock.recv(BUFFSIZE)
    if not r_data:
        break
    # 必须进行行处理
    print(r_data.decode('utf-8').strip())
tcpCliSock.close()