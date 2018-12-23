from flask import Blueprint

# 前置的类
route_imooc = Blueprint('imooc_page',__name__)

@route_imooc.route('/')
def index():
    return "imooc index page"

@route_imooc.route('/hello')
def hello():
    return 'imooc hello world'



