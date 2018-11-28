import urllib.request


#User-Agent 是爬虫和反爬虫斗争的第一步

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',

}


#通过urllib.request.Request()方法构造一个请求对象
request = urllib.request.Request('http://www.baidu.com',headers = headers)

# print(request)

# 向指定的url地址发送请求,并返回服务器响应的类文件对象
response = urllib.request.urlopen(request)

# 返回http的响应码 
print(response.getcode())

# 发送请求后,给你返回数据的是哪个url
#防止重定向301的问题错误
print(response.geturl())


#返回服务器响应的http报头
print(response.info())

#服务器返回的类文件对象支持python文件对象的操作方法
# read()读取文件里的内容
html = response.read()

# print(html)