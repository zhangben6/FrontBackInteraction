import pymysql
db = pymysql.connect('localhost','root','123456',charset='utf8')
cur = db.cursor()
cur.execute('use ajaxdemo')
name = input('请输入姓名:')
password = input('请输入密码:')
try:
    ins = 'insert into user(username,password) values(%s,%s)'
    cur.execute(ins,[name,password])
    db.commit()
    print('添加成功')
except Exception as e:
    print("服务器异常",e)
    db.rollback()
cur.close()
db.close()