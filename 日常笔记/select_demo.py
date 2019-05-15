# 基于select的io多路复用监听服务器
from socket import *
import select


s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

    
