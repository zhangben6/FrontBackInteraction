'''
1.urllib的基本使用方法
引用urllib库中的request模块中的urlopen方法得到目标url的html内容
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
    url:需要打开的网址
    data:Post提交的数据(用户提交的数据)
    timeout:设置网站的访问超时时间
直接用urllib.request模块的urlopen（）获取页面，page的数据格式为bytes类型，需要decode（）解码，转换成str类型
不多BB,上代码  ↓↓↓
'''
from urllib import request
response = request.urlopen(r"https://python.org/")
print(response)      #<http.client.HTTPResponse object at 0x0000000002D46EB8> 响应HTTPResponse对象的名字
page = response.read()
page1 = response.info()  #返回HTTPResponse对象，表示远程服务器返回的头的详细信息
page2 = response.getcode()
print(page.decode())

'''
2.使用Request
    urllib.request.Request(url, data=None, headers={}, method=None)
    **使用request（）来包装请求**，再通过urlopen（）获取页面。
'''
url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
req = request.Request(url, headers=headers)  #传入修改或者增加headers的信息参数,重新生成新的url
page = request.urlopen(req).read()
page = page.decode('utf-8')
'''用来包装头部的数据：
        User-Agent ：这个头部可以携带如下几条信息：浏览器名和版本号、操作系统名和版本号、默认语言
        Referer：可以用来防止盗链，有一些网站图片显示来源http://***.com，就是检查Referer来鉴定的
        Connection：表示连接状态，记录Session的状态。
'''



'''
3.post提交数据方式
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
    urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
'''
from urllib import request,parse
url = r'http://www.lagou.com/jobs/positionAjax.json?'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
data = {
    "first":"true",
    'pn':1,
    'kd':'Pyhton'
}

#urlencode()主要作用就是将url附上客户端post提交的数据,将data数组中的数据转换为url格式
data = parse.urlencode(data).encode('utf-8')
print(data)    # b'first=true&pn=1&kd=Pyhton'
req_url = request.Request(url,headers=headers,data=data)
page = request.urlopen(req_url).read()
page = page.decode('utf-8')


'''
重要的东西来了哈:
4.urllib.error异常处理
urllib.error可以接收有urllib.request产生的异常.
urllib.error有两个方法，URLError和HTTPError可以处理产生的异常
'''
#先看下URLError的异常
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.churentoudi666.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)  #运行结果为:[Errno 11004] getaddrinfo failed  获取地址失败  


#再看下error模块第二个处理异常的方法(HTTPError)
from urllib import request
from urllib import error
'''运行之后，我们可以看到403，这
说明请求的资源没有在服务器上找到，
www.douyu.com这个服务器是存在的，
但是我们要查找的Jack_Cui.html资源
是没有的，所以抛出403异常。
'''
if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        # html = responese.read()
    except error.HTTPError as e:
        print(e.code)


'''5.URLError和HTTPError的混合使用
如果想用HTTPError和URLError一起捕获异常，
那么需要将HTTPError放在URLError的前面，
因为HTTPError是URLError的一个子类。如果URLError放在前面，
出现HTTP异常会先响应URLError，这样HTTPError就捕获不到错误信息了。
'''
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
    except error.HTTPError as e:
            print("HTTPError")
            print(e.code)
    except error.URLError as e:
            print("URLError")
            print(e.reason)

