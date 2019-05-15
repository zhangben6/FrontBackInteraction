# 基于poll的io多路复用

from socket import *
import select

s = socket()
s.setsockopt


while True:
    # 监控关注的IO
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from ',addr)
            
            # 将客户端套接字添加关注并添加到字典中
            p.register(c)
            fdmap[c.fileno()] = c
        else:
            # 客户端套接字准备就绪
            data = fdmap[fd].recv(1024).decode()
            # 如果客户端退出，则不在关注，并从字典中移出
            if not data:
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
                fdmap[fd].send(b'收到你的消息了'.encode())

s.close()
