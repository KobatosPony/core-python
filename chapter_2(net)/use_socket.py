import socket

# socket(socket_family, socket_type, protocol=0) protocol一般不指定
# 创建 TCP/IP 套接字
tcpSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 创建 UDP/IP 套接字
udpSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 常见的套接字对象方法和属性
# 服务器套接字方法
# s.bind() 将地址（主机名、端口号对）绑定到套接字上
# s.listen() 设置并启动 TCP 监听器
# s.accept() 被动接受 TCP 客户端连接，一直等待直到连接到达（阻塞）
# 客户端套接字方法
# s.connect() 主动发起 TCP 服务器连接
# s.connect_ex() connect()的扩展版本，此时会以错误码的形式返回问题，而不是抛出一个异常
# 普通的套接字方法
# s.recv() 接收 TCP 消息
# s.recv_into()①
# 接收 TCP 消息到指定的缓冲区
# 本文档由Linux公社 www.linuxidc.com 收集整理
# 50 第 1 部分 通用应用主题
# （续表）
# 名 字 描 述
# s.send() 发送 TCP 消息
# s.sendall() 完整地发送 TCP 消息
# s.recvfrom() 接收 UDP 消息
# s.recvfrom_into()
# 接收 UDP 消息到指定的缓冲区
# s.sendto() 发送 UDP 消息
# s.getpeername() 连接到套接字（TCP）的远程地址
# s.getsockname() 当前套接字的地址
# s.getsockopt() 返回给定套接字选项的值
# s.setsockopt() 设置给定套接字选项的值
# s.shutdown() 关闭连接
# s.close() 关闭套接字
# s.detach() 在未关闭文件描述符的情况下关闭套接字，返回文件描述符
# s.ioctl()
# 控制套接字的模式（仅支持 Windows）
# 面向阻塞的套接字方法
# s.setblocking() 设置套接字的阻塞或非阻塞模式
# s.settimeout() 设置阻塞套接字操作的超时时间
# s.gettimeout() 获取阻塞套接字操作的超时时间
# 面向文件的套接字方法
# s.fileno() 套接字的文件描述符
# s.makefile() 创建与套接字关联的文件对象
# 数据属性
# s.family① 套接字家族
# s.type① 套接字类型
# s.proto① 套接字协议