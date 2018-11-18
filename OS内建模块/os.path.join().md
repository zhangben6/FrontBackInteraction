## python路径拼接os.path.join()函数

#### Pyhon中有join()和os.path.join()两个函数,具体作用如下:
- ***join()*** ： 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
- ***os.path.join()*** ： 将多个路径组合后返回

# 两个函数的说明 
## 1、join()函数 
- 语法： ‘sep’.join(seq)  
- 参数说明  sep：分隔符(可以为空)   
- seq：要连接的元素序列、字符串、元组、字典 
- 上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串  
- 返回值：返回一个以分隔符sep连接各个元素后生成的字符串   
## 2、os.path.join()函数   
- 语法： os.path.join(path1[,path2[,……]])   
- 返回值：将多个路径组合后返回


### **进入主题**-->
- os.path.join()函数用于路径拼接文件路径。os.path.join()函数中可以传入多个路径：

- 需要导入 import os

```py  
import os  
print("1:",os.path.join('aaaa','/bbbb','ccccc.txt'))  
print("2:",os.path.join('/aaaa','/bbbb','/ccccc.txt'))  
print("3:",os.path.join('aaaa','./bbb','ccccc.txt'))  
特殊情况  
print("4:",os.path.join('/hello/','zhang/ben/','ccccc.txt'))  
```
```
1: /bbbb\ccccc.txt  
2: /ccccc.txt  
3: aaaa\./bbb\ccccc.txt  
4: /hello/zhang/ben/ccccc.txt  
```



- 前两行代码以”/”开头的参数开始拼接，之前的参数全部丢弃
- 若出现”./”开头的参数，会从”./”开头的参数的上一个参数开始拼接

### 总结一下:其实只是2种不同写法而已，都可以达到相同的拼接效果的。看自己的喜好来写吧