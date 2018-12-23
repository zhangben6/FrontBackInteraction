#框架服务器
from socket import *
from settings import *


#静态网页的位置
STATIC_DIR = './static'

#WebFrame服务器类
class WebFrame(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)        
        self.sockfd.bind(frame_address)
    
    #启动服务器:监听,接收连接请求
    def start(self):
        self.sockfd.listen(5) #监听
        print('webframe started....')
        while True:
            connfd,addr = self.sockfd.accept()
            method = connfd.recv(128).decode()
            path_info = connfd.recv(1024).decode()
            
            #处理httpserver的请求函数
            self.handle(connfd,method,path_info)

    #处理请求,读取文件
    def handle(self,connfd,method,path_info):
        if method == 'POST':
            pass
        elif method =='GET':
            if path_info == '/':
                resp = self.get_html('/index.html')
            else:
                resp = self.get_html(path_info)
        connfd.send(resp.encode()) #发送Frame服务器的文件文本内容
        connfd.close() #关闭socket
            
    #读文件
    def get_html(self,path_info):
        full_path = STATIC_DIR + path_info
        print('full_path',full_path)
        try:
            fd = open(full_path)
        except:
            resp = '404'
            print('open file err')
        else:
            resp = fd.read()  #读文件内容
            fd.close()
        return resp

if __name__ == '__main__':
    webfram = WebFrame()
    webfram.start()


