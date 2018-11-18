from socket import * 
# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",5000))
s.listen(5)
print("waiting for ....")
while True:
    c,addr = s.accept()
    print("connect from :",addr)
    # 浏览器的请求
    data = c.recv(4096)
    print(data)

    # 返回http响应
    data = '''Http/1.1 200 OK
    Content-Encoding:utf8
    Content-type:text/html

    <h1>Welcome to tedu</h1>
    <p>Python</P>
    <textarea id="text1"></textarea>
    <button>commit</button>
    <textarea id="text2"></textarea>
    '''
    c.send(data.encode())
    print(111)
    c.close()
s.close()

