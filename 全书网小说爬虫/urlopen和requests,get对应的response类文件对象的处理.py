from urllib.request import urlopen
import chardet
import requests

# #1. 使用requests模块中的get方法获取html字符串
response = requests.get('http://tieba.baidu.com/f?kw=python&pn=100')
response.encoding = 'utf-8'
print(response.text)

# 2.使用urllib.request模块中的urlopen方法获取html字符串
response = urlopen('http://tieba.baidu.com/f?kw=python&pn=100')
html_bytes = response.read()
html = html_bytes.decode('utf-8')
print(html)

#3.拓展: html下载器: 导入一个可以发送请求的类
from requests import Session
url = 'http://tieba.baidu.com/f?kw=python&pn=100'
response = Session().get(url)
response.encoding = 'utf-8'
print(response.text)

# 4.利用chardet模块可以获取response的编码格式
import chardet
response=urlopen('http://tieba.baidu.com/f?kw=python&pn=100',timeout=3)
html_byte=response.read()
chardit1 = chardet.detect(html_byte)
print(chardit1['encoding'])  
html_string=html_byte.decode('utf-8')
html_string=html_byte.decode(chardit1['encoding'])
print(type(html_string))

