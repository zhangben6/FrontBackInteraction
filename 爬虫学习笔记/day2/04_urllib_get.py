'''
通过使用百度url
搜索需要查询的关键字
最终返回页面的源文件
'''

import urllib.parse
import urllib.request

url = 'http://www.baidu.com/s'

headers = {
    'User-Agent':'Mozilla......'
}
 
keyword = input('please input you want enter TheKeyword :')

wd = {'wd':keyword}
# url编码搜索的字符串
new_wd = urllib.parse.urlencode(wd)

#拼接完整的url请求地址
fullurl = url + '?' + new_wd
print(fullurl)
#通过urllib.request.Request()构造一个请求对象
request = urllib.request.Request(fullurl,headers = headers)

#模仿浏览器发送http请求,并返回服务器响应的类文件对象
response = urllib.request.urlopen(request)
# print(response.read())
