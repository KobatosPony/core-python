# 使用socketserver 创建TCP服务器

from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as  SRH)
from time import ctime


HOST = ''
PORT = 12345
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('....connected from:', self.client_address)
        self.wfile.write('[%b] %b'.encode('utf-8') %(ctime().encode('utf-8'),self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()

# 我们得到了请求处理程序 MyRequestHandler，作为 SocketServer
# 中 StreamRequestHandler 的一个子类，并重写了它的 handle()方法，该方法在基类 Request 中
# 默认情况下没有任何行为。
# def handle(self):
#  pass
# 当接收到一个来自客户端的消息时，它就会调用 handle()方法。而 StreamRequestHandler
# 类将输入和输出套接字看作类似文件的对象，因此我们将使用 readline()来获取客户端消息，
# 并利用 write()将字符串发送回客户端。
# 因此，在客户端和服务器代码中，需要额外的回车和换行符。实际上，在代码中你不会
# 看到它，因为我们只是重用那些来自客户端的符号。除了这些细微的差别之外，它看起来就
# 像以前的服务器。