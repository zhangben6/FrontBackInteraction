import urllib.request
import urllib.parse

def loadPage(url,filename):
    '''
    作用:根据url发送请求,获取服务器响应文件
    url:需要爬取和下载的url内容
    filename:需要处理的文件名
    '''
    print('正在下载' + filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)    
    return response.read()



def writePage(html,filename):
    '''
        作用:将heml内容写入到本地
        html:服务器相应文件内容
    '''
    print('正在保存'+filename)
    with open(filename,'w') as f:
        f.write(html)
    print('-' * 30)

def tiebaSpider(url,beginPage,endPage):
    '''作用:贴吧爬虫调度器,负责组合处理每个页面的url
        url:贴吧url的前部分(不包含数据的查询项)
        beginPage:起始页
        endPage:结束页
    '''
    for page in range(beginPage,endPage+1):
        pn = (page - 1) * 50
        filename = '第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        # print(fullurl) #debug
         
        #把拼接好需要下载的url传给loadpage函数
        html = loadPage(fullurl,filename)
        # print(html)
        writePage(html,filename)
    print('谢谢使用')
 
     
if __name__ == '__main__':
    kw = input("please enter you The Tieba name:")
    beginPage = int(input('please enter the start page:'))
    endPage = int(input('please enter the last page:'))

    url = 'http://tieba.baidu.com/f?'
    new_kw = urllib.parse.urlencode({'kw':kw})
    fullurl = url + new_kw
    tiebaSpider(fullurl,beginPage,endPage)

