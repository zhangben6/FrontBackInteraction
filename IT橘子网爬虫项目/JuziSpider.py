#!/爬虫/venv/bin python3.7
# -*- coding: utf-8 -*-

import json
import time
import re
import os
import threading
import requests
import pymysql
from selenium import webdriver

class Spider:
    """
    爬虫基类
    """
    TAG = True # 监控状态的变量

    def __init__(self, payload, token, cookie, page):
        self.authorization = token
        self.cookie = cookie
        self.payloadData = payload
        self.page = page

    def get_contents(self):
        """
        入口主函数 根据payload条件列表获取项目基本信息
        """
        api_url = "https://itjuzi.com/api/companys"
        headers1 = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Authorization': self.authorization,
            'Connection': 'keep-alive',
            'Content-Length': '203',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': self.cookie,
            'CURLOPT_FOLLOWLOCATION': 'true',
            'Host': 'itjuzi.com',
            'Origin': 'https://itjuzi.com',
            'Referer': 'https://itjuzi.com/company',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '73.0.3683.75 Safari/537.36',
        }
        self.payloadData['page'] = self.page
        response = requests.post(url=api_url, headers=headers1, data=json.dumps(self.payloadData))


        if response.status_code == 200:
            response.encoding = 'utf-8'
            page_datas = json.loads(response.text)['data']['data']
            print(page_datas)
            for project in page_datas:
                project_name = project['name']
                company_name = project['register_name']
                # print(project_name,company_name)
                found_time = project['agg_born_time']
                current_round = project['round']
                total_money = project['total_money']  # 已经获投总额
                tags_li = []
                if len(project['tag']) > 0:
                    for dic in project['tag']:
                        tags_li.append(dic['tag_name'])
                tags = ','.join(tags_li)
                industry = project['scope']  # 行业分类
                sub_industries = project['sub_scope']  # 子行业
                description = project['des']
                province = project['prov']
                city = project['city']
                cdn = project['logo']
                name = re.findall(r'.*/(.*(png|jpg|jpeg|icon)).*', cdn)[0][0]
                fin_needs = self.payloadData['com_fund_needs']  # 需要需求
                local = 1 if project['location'] == 'in' else 0
                status = project['status']  # 经营状态
                base_info = [project_name, company_name, found_time, tags, current_round, total_money,industry,
                             sub_industries, description, province, city, fin_needs, local, status]
    #
                # print(base_info)
    #
                # 判断数据库是否存在该项目信息
                pro_id = self.query_pro_id(project_name, company_name)
                if not pro_id:
                    # 主项目信息表更新
                    sql1 = r"insert into pro_base_info (project_name,company_name,found_time,tags," \
                           r"current_round,total_money,industry,sub_industries, description,province," \
                           r"city,fin_needs,local,status,image,update_time,add_time)values" \
                           r"(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    logo_path = self.deal_images(cdn, name)
                    cur_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    base_info.append(logo_path)  #图片路径 image
                    base_info.append(cur_time)   #当前时间 图片 update_time
                    base_info.append(cur_time)   #add_time
                    print(base_info)
                    self.insert_to_db(sql1, base_info)       # sql1语句 和 base_info 17个信息的列表
                else:
                    lo = "<{}>信息已经入库".format(project_name)
                    self.log(lo)
        else:   #获取状态码不为200 资源获取有误
            Spider.TAG = False
            lo = "error page:{}".format(self.page)
            self.log(lo)
    # #
    def deal_images(self, cdn, name):
        """
        logo 下载
        :param cdn: url
        :param name: 保存名字
        :return: 保存的路径 (结合web后台)
        """
        response = requests.get(cdn)     #获得网站上的图片路径
        data = response.content          #返回的是 bytes 型的二进制数据
        path = "logos/{}".format(name)   #图片名及路径
        save_path = path
        if not os.path.exists(save_path):       # save_path 保存图片
            with open(save_path, 'wb') as f:
                f.write(data)
        return path
    #
    # #
    # #把信息插入到数据库中
    def insert_to_db(self, sql, data):
        """
        数据库 新增函数
        :param sql:
        :param data:
        :return:
        """
        con = pymysql.Connect(
            host="localhost",
            user="root",
            database="test",
            password="asd7758521",
            charset="utf8",
            port=3306
        )
        #创建游标
        cursor = con.cursor()
        try:
            cursor.execute(sql, data)    #添加到缓存中
            con.commit()
        except Exception as error:
            con.rollback()    #???? 回转？
            print(error)
        cursor.close()
        con.close()
    #
    #
    def query_pro_id(self, project_name, company_name):
        """
        项目查询函数
        :param project_name: 项目名称
        :param company_name: 公司名称
        :return: None/tuple 示例 （1,)
        """
        con = pymysql.Connect(
            host="localhost",
            user="root",
            database="test",
            password="asd7758521",
            charset="utf8",
            port=3306
        )
        cursor = con.cursor()
        sql = "SELECT id FROM pro_base_info WHERE project_name='%s' AND company_name='%s'" \
              % (project_name, company_name)
        cursor.execute(sql)
        pro = cursor.fetchone()
        cursor.close()
        con.close()
        return pro
    #
    # #
    def log(self, datas):
        """
        自定义日志记录 （也可以使用logging模块)
        :param datas:
        :return:
        """
        with open('log.txt', 'a+', encoding="utf-8") as f:
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write("{}".format(cur_time) + datas + '\n')



#
# if __name__ == "__main__":
#     payloadData = {
#         'city': [],
#         'com_fund_needs': "需要融资",
#         'keyword': "",
#         'location': "",
#         'page': 1,
#         'pagetotal': 0,
#         'per_page': 20,
#         'prov': "",
#         'round': [],
#         'scope': "",
#         'selected': "",
#         'sort': "",
#         'status': "",
#         'sub_scope': "",
#         'total': 0,
#         'year': [],
#     }
#     tup = (
#         'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvdXNlcnNcL3VzZXJfaGVhZGVyX2luZm8iLCJpYXQiOjE1NTYxODcwMDIsImV4cCI6MTU1NjE5NjU0NywibmJmIjoxNTU2MTkyOTQ3LCJqdGkiOiJVY3lnSnVNamNKdmx0eFZXIiwic3ViIjo3MTgzNjgsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.roK1ZadjjfIDyHvFqwTfuZ2DdzH2Sv3qn0R3zKc8AvU',
#         'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1556122019; _ga=GA1.2.1099442073.1556122020; _gid=GA1.2.1267569008.1556122020; acw_tc=781bad3015561609590441592e5bf490c0f55b71196c1d5366aedfa2cf157d; gr_user_id=78dcfa69-c844-430d-9114-0bb34b34c7ab; MEIQIA_VISIT_ID=1KLBNydNIpxBovrUZyqe7CKPKWN; MEIQIA_EXTRA_TRACK_ID=1KLBO2Wu1peseKYHAl4kd5j8YKs; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1556186947; juzi_user=718368; juzi_token=bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NTYxODcwMDIsImV4cCI6MTU1NjE5MDYwMiwibmJmIjoxNTU2MTg3MDAyLCJqdGkiOiJNaDdub1MxbFlselZGaWhFIiwic3ViIjo3MTgzNjgsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.TG_Jlw7jV2y5bDk7oTugCDNW_WYU1ctNypG6Ob639i0'
#         )
#     # token / cookie 也可手动获取也可做模拟登陆
#     start_page = 1  # 起始页
#     end_page = 5  # 结束页
#     count = 1
#     while True:
#         spider = Spider(payloadData, tup[1], tup[0], start_page)
#         spider.get_contents()
#         info = spider.get_contents()
#         print(info)
#



if __name__ == "__main__":
    payloadData = {
        'city': [],
        'com_fund_needs': "需要融资",
        'keyword': "",
        'location': "",
        'page': 1,
        'pagetotal': 0,
        'per_page': 20,
        'prov': "",
        'round': [],
        'scope': "",
        'selected': "",
        'sort': "",
        'status': "",
        'sub_scope': "",
        'total': 0,
        'year': [],
    }
    tup = (
        'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaXRqdXppLmNvbVwvYXBpXC9hdXRob3JpemF0aW9ucyIsImlhdCI6MTU1NjI5MTU3MiwiZXhwIjoxNTU2Mjk1MTcyLCJuYmYiOjE1NTYyOTE1NzIsImp0aSI6InIzcXZCbktKSkQ3NGhJWFAiLCJzdWIiOjcxODgwNCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.dz5r4H9qpksuQ_i1H9bw2B92NNNm99OAa9QM0cJ64Q4',
        'acw_tc=7b39758215562510843431346e99dcfddbb945858da0026d13c56e0d3d07b1; _ga=GA1.2.40982581.1556255529; _gid=GA1.2.715200239.1556255529; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1556255529,1556256048,1556258451,1556291549; juzi_user=718804; juzi_token=bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaXRqdXppLmNvbVwvYXBpXC9hdXRob3JpemF0aW9ucyIsImlhdCI6MTU1NjI5MTU3MiwiZXhwIjoxNTU2Mjk1MTcyLCJuYmYiOjE1NTYyOTE1NzIsImp0aSI6InIzcXZCbktKSkQ3NGhJWFAiLCJzdWIiOjcxODgwNCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.dz5r4H9qpksuQ_i1H9bw2B92NNNm99OAa9QM0cJ64Q4; _gat_gtag_UA_59006131_1=1; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1556291663'
    )
    # token / cookie 也可手动获取也可做模拟登陆
    start_page = 2  # 起始页
    end_page = 5  # 结束页
    count = 1

     ###########################
    while True:
        spider = Spider(payloadData, tup[1], tup[0], start_page)
        # try:
        #     spider.get_contents()
        # except Exception as e:
        #     print(e)
        #     break
        spider.get_contents()

        if not Spider.TAG:
            tup = ('new_token', 'new_cookie')
            count += 1
            if count >= 5:
                break
        else:
            start_page += 1
            if start_page > end_page:
                break