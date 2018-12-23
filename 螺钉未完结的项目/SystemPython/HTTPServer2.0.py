

from socket import *
from threading import Thread
import sys

class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        self.create_socket()

    def create_socket(self):
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
                sys.exit("退出程序")
            except Exception as e:
                print(e)
                continue
            clinetThread = Thread(target=self.handle,args=(connfd,))
            clinetThread.setDaemon(True)
            clinetThread.start()
        
    def handle(self,connfd):
        request = connfd.recv(4096)
        requestHeaders = request.decode().splitlines()
        # print(requestHeaders)        
        # print(connfd.getpeername(),":",requestHeaders[0])
        get_request = requestHeaders[0].split(" ")[1]
        print(get_request)
        if get_request == "/" or get_request[-5:]==".html":
            self.get_DataPages(connfd,get_request)
        # elif get_request == '/css/index.css':
        #     self.get_css(connfd,get_request)
        elif get_request[-4:] == '.css':
            self.get_DataPages(connfd,get_request)

        elif get_request[-4:] == '.png' or get_request[-4:] == '.jpg':
            self.get_image(connfd,get_request)


    def get_DataPages(self,connfd,get_request):
        # print('hello world')
        if get_request == '/':
            filename = self.static_dir +  "/index.html"
        else:
            filename = self.static_dir + get_request
        try:
            f = open(filename)
        except Exception:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            # responseHeaders = "Content-type:text/html;charset=utf-8\r\n"
            responseHeaders += "\r\n"
            responseBody = "SORRY,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            # responseHeaders = "Content-type:text/html;charset=utf-8\r\n"
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
        filename = self.static_dir + get_request
        print(filename)
        try:
            f = open(filename,'rb')
        except Exception:
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
            response = responseHeaders.encode('utf8') + responseBody
            connfd.send(response)


server_addr = ('0.0.0.0', 8000)
static_dir = "C:/Users/Administrator/Desktop/SystemPython"
httpd = HTTPServer(server_addr,static_dir)
httpd.serve_forever()

