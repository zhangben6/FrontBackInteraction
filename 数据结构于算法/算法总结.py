# coding:utf-8


import time

'''冒泡排序'''
def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):  # 外层控制循环的次数
        count = 0
        for i in range(n-1-j):  # 内存控制指针的步数
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:  # 如果有循环没有改变值的情况，return
            print(alist)
            return 
    print(alist)

# bubble_sort([4,1,2,5,3,6,9,87,7,234,34,65,37,10,100,236])


'''选择排序'''
def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]
    print(alist)

# select_sort([4,1,2,5,3,6,9,87])


'''插入排序'''
def insert_sort(alist):
    n = len(alist)
    for j in range(1,n):
        while j > 0:
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
                j -= 1
            else:  # 加入了else判断，优化了时间复杂度为o(n)
                break
    print(alist)
# insert_sort([4,1,2,5,3,6,9,87])



'''希尔排序'''
# 希尔排序是在插入排序的基础上做了一些修改优化(未完成)
# def shell_sort(alist):
#     n = len(alist)
#     gap = n // 2
#     i = 1
#     if alist[i] < alist[i-gap]:
#         alist[i-gap],alist[i] = alist[i],alist[i-gap]
#     else:
#         break



'''快速排序''' 
def quick_sort(alist,first,last):

    # 递归的终止条件
    if first >= last:
        return 

    mid_value = alist[first]  # 之后开始移动high游标
    # 中间值
    low = first
    high = last
    while low < high:
        # 让high游标左移
        while low < high and alist[high] >=  mid_value:
            high -= 1
        alist[low] = alist[high]
        # low += 1 

        # 让low游标右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        # high -= 1 

    # 此时循环退出，low==high
    alist[low] = mid_value

    # 递归处理左右两边的序列
    quick_sort(alist,first,low-1)

    quick_sort(alist,low+1,last)


# if __name__ == '__main__':
#     li = [34,234,54,23,78,54,6342,90,12,344,6,5,7675,324]
#     print(li)
#     quick_sorted(li,0,len(li)-1)
#     print(li)

         





