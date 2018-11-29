# _*_ coding:utf-8 _*_
'''
    python3.6
    author: 张奔
    github: http://www.github.com/zhangben6/FrontBackInteraction
    项目名称: 全书网小说爬虫开发
'''
import requests 
import re


class NovelSpider():
    '''全书网爬虫Spider类'''
    def __init__(self):
        self.session = requests.Session()  #下载器类,含有get请求的方法
        
    def get_nov(self,url):
        '''下载小说 | 主逻辑函数 '''
        #以盗墓笔记为例,下载首页面
        index_html = self.download(url,encoding='gbk')
        # print(index_html)

        #小说的标题
        title = re.findall(r'"article_title">(.*?)</a>',index_html)[0]
        print(title)

        #提取盗墓笔记章节的url网址
        novel_chapter_infos = self.get_chapter_info(index_html)

        #创建一个文件  小说名.txt
        f = open('%s.txt' % title,'w')


        #循环下载盗墓笔记章节信息
        for chapter_info in novel_chapter_infos:
            #写章节题目
            f.write('%s\n' % chapter_info[1])

            #下载章节内容
            content = self.get_chapter_content(chapter_info[0])




    def download(self,url,encoding):
        '''下载html源码'''
        response = self.session.get(url)
        response.encoding = encoding
        html = response.text
        return html
    
    
    def get_chapter_info(self,index_html):
        '''利用正则提取章节url信息'''
        div = re.findall(r'<DIV class="clearfix dirconone">(.*?)</DIV>',index_html,re.S)[0]
        # print(div)

        #用正则二次过滤符合条件的数据
        info = re.findall(r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>',div)
        # print(info)
        return info



    def get_chapter_content(self,chapter_url):
        '''下载章节内容函数'''

        chapter_html = self.download(chapter_url,encoding='gbk')
        content = re.findall(r'<script type="text/javascript">style5\(\);</script>(.*?)<script',chapter_html,re.S)[0]

        #清洗数据
        content = content.replace('&nbsp;','')
        content = content.replace('<br />','')
        #替换换行
        content = content.replace('\r\n','')
        print(content)
        exit()



if __name__ == '__main__':
    nover_url = 'http://www.quanshuwang.com/book/9/9055'
    spider = NovelSpider()
    spider.get_nov(nover_url)

    

