# -*- coding:utf-8 -*-
from socket import *
from threading import Thread
import sys
import re




class HTTPServer(object):
    def __init__(self,static_dir,server_addr):
        self.static_dir = static_dir
        self.server_address = server_addr
        self.ip = server_addr[0]
        self.port = server_addr[1]
        
        self.create_socket()
    
    def create_socket(self):
        self.sockfd = socket(AF_INET,SOCK_STREAM)
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        print(self.server_address)
        self.sockfd.bind(self.server_address)
    
    def server_forever(self):
        self.sockfd.listen(10)
        print('Listen to the port ',self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务端退出")
            except Exception as e:
                print(e)
                continue
            ClientThread = Thread(target=self.handle,args=(connfd,))
            ClientThread.setDaemon(True)
            ClientThread.start()
    
    # 处理客户端请求的函数
    def handle(self,connfd):
        request_data = connfd.recv(4096)
        if not request_data:
            connfd.close()
            return
        resquestHeaders = request_data.decode('utf-8').splitlines()
        print(resquestHeaders[0])
        # print(resquestHeaders)
        
        #正则提取请求行信息
        pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH_INFO>/\S*)'
        
        try:
            p = re.match(pattern,resquestHeaders[0])
            env = p.groupdict()
            print(env)
        except:
            response = 'HTTP/1.1 500 SERVER ERROR\r\n'
            response += '\r\n'
            response +='Server error'
            connfd.send(response.encode()) #发送响应
            connfd.close()
            return
        

        content = self.DataInteraction(**env)
        if content == '404':
            header ='HTTP/1.1 404 Not Found\r\n'
            header += '\r\n'
            body = 'Sorry,not found the webpage'
            response = header + body
        elif 4 < len(content) < 10:
            if content == "admin":
                data = '{"status":1,"message":"用户名已经存在"}'
            else:
                data = '{"status":1,"message":"用户名可以使用"}'
            header = 'HTTP/1.1 200 OK\r\n'
            header += "Content-Encoding:utf-8\r\n"
            header += "Content-Type:text/html\r\n"  
            header += 'HTTP/1.1 200 OK\r\n'
            header += '\r\n'
            response = header + data
            connfd.send(response.encode('utf-8'))
            connfd.close()
            return
        else:
            header = 'HTTP/1.1 200 OK\r\n'
            header += '\r\n'
            response = header + content

            #服务器最终向客户端发送的内容
            connfd.send(response.encode('utf-8'))
            connfd.close()
    
    def DataInteraction(self,METHOD,PATH_INFO):
        if METHOD == 'GET':
            if PATH_INFO == '/':
                PATH_INFO = '/index.html'
            elif PATH_INFO[:6] == '/index':
                userdata = PATH_INFO[7:]
                username = userdata.split('=')[1]
                return username
            filename = static_dir + PATH_INFO
            try:
                f = open(filename)
            except:
                content = '404'
                print('open file err')
            else:
                content = f.read()
            return content
            
        elif METHOD == 'POST':
            pass


server_addr = ('0.0.0.0', 8550)
static_dir = r'C:/Users/Administrator/Desktop/exercise/Ajax-demo'
httpd = HTTPServer(static_dir,server_addr)
httpd.server_forever()



