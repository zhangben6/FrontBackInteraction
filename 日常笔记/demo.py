# class Parent(object):
#     x = 1

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# print(Parent.x,Child1.x,Child2.x)
# Child1.x = 2
# Child2.x = 3
# print(Parent.x,Child1.x,Child2.x)



# # try-except-else-finally的综合用法

# try:
#     print('a')
#     for a in range(10):
#         print(a)
#     print('b')
# except:
#     print('程序捕捉到错误')
# else:
#     print('c')
# finally:
#     print('程序结束')


# def div1(x,y):
#     print('%s/%s = %s'%(x,y,x/y))

# def div2(x,y):
#     print('%s//%s = %s'%(x,y,x//y))

# div1(5,2)
# div1(5.,2)
# div2(5,2)
# div2(5.,2)

# 1~100的求和
# print(sum([x for x in range(1,101)]))

# l = [2,3,4,4,5,5,6,6,723,34,5,54,23]
# l.sort(reverse=True)
# print(l)

# l = [2,3,4,4,5,5,6,6,723,34,5,54,23]
# print(set(l))

# str = '<p><img src="/media/goods/images/image_20190423153430_818.png" title="" alt="image.png"/> </p><p><img src="/media/goods/desc/微信图片_20190315113106_20190423155554_317.jpg" title="" alt="微信图片_20190315113106.jpg"/> </p><p><img src="/media/goods/images/image_20190423153502_255.png" title="" alt="image.png"/> </p><p><img src="/media/goods/images/image_20190423153516_460.png" title="" alt="image.png"/> </p><p><img src="/media/goods/images/image_20190423153532_622.png" title="" alt="image.png"/> </p>'
# str1 = str.split()

import dis
def update_list(l): 
    l[0] = 1

dis.dis(update_list)