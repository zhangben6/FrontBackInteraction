'''Return different web pages based on user requestes
    Ruturn the HTML  web page to the client
            HTTPServer 2.0
'''
from socket import *
import re

def client_requ(client):
    '''处理用户的请求'''
    #获取用户发送的数据
    recv_data = client.recv(1024).decode('utf-8')
    # print(recv_data)
    #提取用户请求的地址
    match = re.match('[^/]+(/[^ ]*) ',recv_data)
    print(match.group(1))
    if match:
        recv_path = match.group(1)
        if recv_path == '/':
            recv_path = 'index.html'
        elif recv_path == '/login':
            recv_path = 'login.html'
        else:
            client.close()
            return 
    '''判断用户的地址,并根据不同的地址返回不同的结果'''
    #响应行
    response_line = 'HTTP/1.1 200 OK\r\n'

    #响应头
    response_head = "Content-type:text/html;charset=utf-8\r\n"

    #判断请求地址
    if recv_path =='index.html':
        response_body = '<h1>郭童我喜欢你</h1>'
    elif recv_path == 'login.html':
        with open("./login.html",encoding='utf-8') as f:
            response_body = f.read()
    else:
        response_line = 'HTTP/1.1 400 NOT FOUND\r\n'
        response_body = '404...  页面不存在'
    response_data = response_line + response_head + '\r\n' + response_body

    #向客户端发送数据
    client.send(response_data.encode('utf-8'))

    client.close()

def main():
    #创建流式套接字
    tcp_server = socket()
    tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcp_server.bind(("0.0.0.0",8000))
    tcp_server.listen(128)
    
    #处理用户请求
    while True:
        client,address = tcp_server.accept()
        client_requ(client)
    tcp_server.close()


if __name__ == '__main__':
    main()