# _*_ conding:utf-8 _*_
''' 
项目:网页服务器部署员工管理系统
HTTP SERVER v2.0
解析具体request
使用多线程并发处理能返回简单数据
使用类封装

author:张奔
addr:https:www.github.com/zhanben6/Python

'''


from socket import *
from threading import Thread
import sys


# 封装httpserver 功能
class HTTPServer(object):
    def __init__(self,server_addr,static_dir,css_dir,images_dir):
        self.server_address = server_addr
        self.css_dir = css_dir
        self.static_dir = static_dir
        self.images_dir = images_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        
        # 创建套接字
        self.create_socket()

    def create_socket(self):
        '''用于创建套接字'''
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)
        

    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen to the port",self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print(e)
                continue

            # 创建线程处理客户端请求
            clinetThread = Thread(target=self.handle,args=(connfd,))
            clinetThread.setDaemon(True)
            clinetThread.start()
        
    # 处理客户端请求
    def handle(self,connfd):
        # 接受request
        request = connfd.recv(4096)
        requestHeaders = request.decode().splitlines()
        post_request = requestHeaders[-1]
        print()        
        # print(connfd.getpeername(),":",requestHeaders[0])
        # 切割
        get_request = requestHeaders[0].split(" ")[1]
        print(get_request)
        if get_request == "/" or get_request[-5:]==".html":
            self.get_html(connfd,get_request)

        # elif get_request == '/css/index.css':
        #     self.get_css(connfd,get_request)
        elif get_request[-4:] == '.css':
            self.get_css(connfd,get_request)

        elif get_request == '/images/timg.gif':
            self.get_image(connfd,get_request)

        # elif get_request == '/js/index.js':
        #     self.get_js(connfd,get_request)
        elif get_request[-3:] == '.js':
            self.get_js(connfd,get_request)

        #想获取数据
        else:
            self.get_data(connfd,get_request)
        connfd.close()


    def get_html(self,connfd,get_request):

        if get_request == '/':
            filename = self.static_dir+ "/index.html"
        else:
            filename = self.static_dir+get_request
        try:
            f = open(filename)
        except Exception:
            #没找到网页
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = "SORRY,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = ''
            while True:
                data = f.read(1024)
                if not data:
                    break
                responseBody += data
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode('utf-8'))

    def get_data(self,connfd,get_request):
        urls = ['/time','/web','/python']
        if get_request in urls:
            if get_request == '/time':
                import time
                response_Body = time.ctime()
            elif get_request == '/web':
                response_Body = 'Web Frame'
            elif get_request == '/python':
                response_Body = 'Python'
        
            response_line = "HTTP/1.1 200 OK\r\n"
            response_head = ''
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_head = "Content-type:text/html;charset=utf-8\r\n"
            response_Body = '<h1>404  没想到吧.............................</h1>'
        response = response_line + response_head +'\r\n' + response_Body
        connfd.send(response.encode())

    def get_css(self,connfd,get_request):
        filename = self.css_dir + get_request
        try:
            f = open(filename)
        except Exception:
            #没找到网页
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = "SORRY,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = ''
            while True:
                data = f.read(1024)
                if not data:
                    break
                responseBody += data
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())
        
    def get_image(self,connfd,get_request):
        filename = self.images_dir + get_request
        try:
            f = open(filename,'rb')
        except Exception:
            #没找到网页
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = "SORRY,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = b''
            while True:
                data = f.read(1024)
                if not data:
                    break
                responseBody += data
        finally:
            response = responseHeaders.encode() + responseBody
            connfd.send(response)


    def get_js(self,connfd,get_request):
        filename = self.images_dir + get_request
        try:
            f = open(filename)
        except Exception:
            #没找到网页
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = "SORRY,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = ''
            while True:
                data = f.read(1024)
                if not data:
                    break
                responseBody += data
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())


# 提供服务器地址和静态文件路径
server_addr = ('0.0.0.0', 7000)
static_dir = "C:/Users/Administrator/Desktop/PersonalSystem/static_WebPages"
css_dir = "C:/Users/Administrator/Desktop/PersonalSystem"
images_dir = "C:/Users/Administrator/Desktop/PersonalSystem"
httpd = HTTPServer(server_addr,static_dir,css_dir,images_dir)
# 调用函数启动服务
httpd.serve_forever()

