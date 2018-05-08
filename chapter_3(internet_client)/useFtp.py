from ftplib import FTP
import sys

encode=['UTF-8','gbk','GB2312','GB18030','Big5','HZ']

# 连接并登陆
def login(address,username,passwd,code='utf-8'):
    # 连接
    f = FTP(address)
    try:
        # 使用用户名和密码登陆
        f.login(username, passwd)
        f.encoding = code
        f.dir()
        return f
    except Exception as e:
        print(e)
        return None


# 尝试解决编码问题
def codeFtp(address,username,passwd):
    for code in encode:
        ftp = login(address,username,passwd,code)
        if ftp is None:
            pass
        else:
            return ftp
    return None

def showDir(f):
    f.dir()

if __name__ == '__main__':
    address = input('请输入地址:')
    username = input('请输入用户名:')
    passwd = input('请输入密码:')

    f = codeFtp(address,username,passwd)
    if not f:
        print('编码失败')
        sys.exit()
    else:
        showDir(f)
        f.pwd()
    f.quit()


# login(user='anonymous',
# passwd='', acct='')
# 登录 FTP 服务器，所有参数都是可选的
# pwd() 获得当前工作目录
# cwd(path) 把当前工作目录设置为 path 所示的路径
# dir ([path[,...[,cb]]) 显示 path 目录里的内容，可选的参数 cb 是一个回调函数，会传递给 retrlines()方法
# nlst ([path[,...]) 与 dir()类似，但返回一个文件名列表，而不是显示这些文件名
# 本文档由Linux公社 www.linuxidc.com 收集整理
# 78 第 1 部分 通用应用主题
# （续表）
# 方 法 描 述
# retrlines(cmd [, cb]) 给定 FTP 命令（如“RETR filename”），用于下载文本文件。可选的回调函数 cb 用于处理文件的每一行
# retrbinary(cmd,
# cb[,bs=8192[, ra]])
# 与 retrlines()类似，只是这个指令处理二进制文件。回调函数 cb 用于处理每一块（块大小默认为 8KB）
# 下载的数据
# storlines(cmd, f) 给定 FTP 命令（如“STOR filename”），用来上传文本文件。要给定一个文件对象 f
# storbinary(cmd, f
# [,bs=8192]) 与 storlines()类似，只是这个指令处理二进制文件。要给定一个文件对象 f，上传块大小 bs 默认为 8KB
# rename(old, new) 把远程文件 old 重命名为 new
# delete(path) 删除位于 path 的远程文件
# mkd(directory) 创建远程目录
# rmd(directory) 删除远程目录
# quit() 关闭连接并退出