from functools import reduce

# print(reduce(lambda x,y:x+y,range(1,10**8)))

# print(sum(range(1,10**8)))

# recursion.py
# def fx(n):
#     print('递归进入第', n, '层')
#     if n == 3:
#         return
#     fx(n + 1)
#     print('递归退出第', n, '层')
# fx(1)
# print("程序结束")

#  试用递归方式实现
#     1 + 2 + 3 + 4 + .... + n 的和
#     如:
#       def mysum(n):
#          ....
#       print(mysum(100))  # 5050



# def mysum(n):
#     if n == 1:
#         return 1
#     return mysum(n-1) + n

# 递归的方式判断字符串是否是回文
s = 'abccba'
def fx(n):
    if n == len(s)-1:
        return s[len(s)-1]
    return fx(n+1) + s[n]

str1 = fx(0)
if str1 == s:
    print('该字符串是回文')
else:
    print('不是回文')
