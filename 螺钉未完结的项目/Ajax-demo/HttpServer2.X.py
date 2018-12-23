#_*_ utf-8 _*_
'''
    Python3.6
    Project:多线程httpserver网络服务器
    author:张奔
    address:https://www.github.com/zhangben6/Python
'''


from socket import *
import sys,os
from threading import Thread
import re
import time

#webFrama通信函数,返回客户端要请求的文件内容
def connect_frame(METHOD,PATH_INFO):
    s = socket()
    try:
        s.connect(frame_address) #连接框架服务器
    except:
        print('Connect err')
        return '401'
    s.send(METHOD.encode())  #发送请求方法
    time.sleep(0.1)
    s.send(PATH_INFO.encode())  #发送请求文件的路径
    
    resp = s.recv(4096).decode()
    if not resp:
        s.close()
        return '404'
    else:
        s.close()
        return resp   #返回文件内容

#封装HTTPServer类
class HTTPServer():
    def __init__(self,address):
        self.address = address
        self.create_socktet()
        self.bind(address) #绑定
        self.server_forever()

    def create_socktet(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self,address):
        self.ip = address[0]
        self.port = address[1]
        self.sockfd.bind(address)

    #启动服务器,调用listen方法
    def server_forever(self):
        self.sockfd.listen(10)
        print('Server start,port on ',self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print('Connect from ',addr)

            #创建处理客户端对象的线程
            handle_client = Thread(
                target=self.handle,
                args = (connfd,))
            
            #设置守护线程,当客户端线程退出时,对应处理线程也会退出
            handle_client.setDaemon(True)

            #启动线程
            handle_client.start()
            

    #定义具体处理客户端请求函数
    def handle(self,connfd):
        #接受来自客户端的数据
        request = connfd.recv(4096)

        # GET /favicon.ico HTTP/1.1
        # User-Agent: Wget/1.17.1 (linux-gnu)
        # Accept: */*
        # Accept-Encoding: identity
        # Host: www.baidu.com
        # Connection: Keep-Alive


        if not request:
            connfd.close()
            return 

        #将请求数据按换行符进行拆分
        request_lines = request.splitlines()

        #获取请求行
        request_line = request_lines[0].decode('utf-8')
        print(request_line)
        
        #判断请求行的合法性
        # pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH_INFO>/\S*HTTP/1.1)'
        pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH_INFO>/\S*)'

        try:
            p = re.match(pattern,request_line)
            env = p.groupdict()
            print(env)
        except:
            response = 'HTTP/1.1 500 SERVER ERROR\r\n'
            response += '\r\n'
            response +='Server error'
            connfd.send(response.encode()) #发送响应
            connfd.close()
            return





        #正常处理 GET /index.html HTTP/1.1
        content = connect_frame(**env) #调用另外的服务
        response = ''

        if content =='404':  #文件未找到
            header ='HTTP/1.1 404 Not Found\r\n'
            header += '\r\n'
            body = 'Sorry,not found the webpage'
            response = header + body

        elif content == '401':
            header ="HTTP/1.1 404 Not Found\r\n"
            header += '\r\n'
            body = 'Sorry,Frame is not opened'
            response = header + body
        
        elif type(content) == 'bytes':
            header ="HTTP/1.1 404 Not Found\r\n"
            header += '\r\n'
            body = 'Sorry,Frame is not opened'
            response = header + content.decode('utf-8')


        else:
            header = 'HTTP/1.1 200 OK\r\n'
            header += '\r\n'
            response = header + content  #将文件内容作为body部分
            
        #服务器最终向客户端发送的内容
        connfd.send(response.encode('utf-8'))
        connfd.close()


server_clientner = HTTPServer(('0.0.0.0',8000))
