from flask import Flask,url_for
from imooc import route_imooc
from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# 设置url搜索路径的统一前缀,让文件更容易管理
app.register_blueprint(route_imooc,url_prefix = '/imooc')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/mysql'
db = SQLAlchemy(app)



@app.route('/')
def hello_world():
    url = url_for('index')
    url_1 = UrlManager.buildUrl("/api ")
    url_2 = UrlManager.buildStaticUrl('css/bootstrap.css')
    msg = 'Hello world,url:%s,url_1:%s,url_2:%s' %(url,url_1,url_2)
    # 日志文件
    app.logger.error(msg)
    app.logger.info(msg)
    return msg


@app.route("/api")
def index():
    return "index page"


@app.route("/api/hello")
def hello(): 
    sql = text('select * from user')
    result = db.engine.execute(sql)
    for row in result:
        app.logger.info(row)
    return 'hello world'


# 日志的错误处理过程,可以打印错误信息
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return 'This page does not exist', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)