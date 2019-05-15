# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 合并链表
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         root = ListNode(Node) # 定义根节点指向头节点用于返回
#         cur = root 
#         while l1 and l2:
#             if l1.val > l2.val:
#                 node = ListNode(l2.val)
#                 l2 = l2.next
#             else:
#                 node = ListNode(l1.val)
#                 l1 = l1.next
#             cur.next = node
#             cur = node
#         # l1和l2有可能有生于元素
#         cur.next = l1 or l2
#         return root.next


# 反转二叉树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if root:
#             root.left,root.right = root.right,root.left
#             self.invertTree(root.left)
#             self.invertTree(root.right)
#         return root
# a = Solution()
# a.invertTree([4,2,7,1,3,6,9])


# 二叉树的层级遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 用栈实现队列

# 首先运用python的collections模块中的deque实现一个栈
# from collections import deque
# class Stack:
#     def __init__(self):
#         self.items = deque()
    
#     def push(self,val):
#         return self.items.append(val)
    
#     def pop(self):
#         return self.items.pop()
    
#     def top(self):
#         return self.items[-1]
    
#     def empty(self):
#         return len(self.items) == 0


# # 队列类
# class MyQueue(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.s1 = Stack()
#         self.s2 = Stack()

 
#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: None
#         """
#         self.s1.push(x)

        

#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         if not self.s2.empty():  # 如果s2不为空
#             return self.s2.pop()
#         # 否则就循环把s1栈中的值全部压到s2中
#         while not self.s1.empty():
#             val = self.s1.pop()
#             self.s2.push(val)
#         return self.s2.pop()
        

#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         if not self.s2.empty():  # 如果s2不为空
#             return self.s2.top()
#         while not self.s1.empty():
#             val = self.s1.pop()
#             self.s2.push(val)
#         return self.s2.top()
        

#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         return self.s1.empty() and self.s2.empty()

# def test():
#     q = MyQueue()
#     q.push(1)
#     q.push(2)
#     q.push(3)
#     print(q.pop())
#     print(q.pop())
#     print(q.pop())
# test()


# 合并n个有序的链表，返回合并后的排序链表

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# from heapq import heapify,heappop
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         if not lists:
#             return []

#         # 读取所有的值放入到一个列表中
#         h = []
#         for node in lists:  
#             while node:   # 这里的node指的是链表的头节点
#                 h.append(node.val)
#                 node = node.next
        
#         # 构建一个最小堆
#         heapify(h)

#         # 构造一个新链表
#         root = ListNode(heappop(h))
#         curnode = root  # 可以理解为指针节点
#         while h:
#             nextnode = ListNode(heappop(h))
#             curnode.next = nextnode
#             curnode = nextnode
#         return root


# collection模块联系
# from collections import namedtuple
 
# websites = [
#     ('Sohu', 'http://www.google.com/', u'张朝阳'),
#     ('Sina', 'http://www.sina.com.cn/', u'王志东'),
#     ('163', 'http://www.163.com/', u'丁磊')
# ]
 
# Website = namedtuple('Website', ['name', 'url', 'founder'])
 
# for website in websites:
#     website = Website._make(website)
#     print(website)

# infos = [('zhangben','male',99),('guotong','female',100),('shiyan','female',101)]
# INFO = namedtuple('shabi',['name','gender','score'])
# for info in infos:
#     info = INFO._make(info)
#     print(info)

import heapq
class TopK:
    def __init__(self,iterable,k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable
    
    def push(self,val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass  # 迭代的元素小于最小堆的栈顶元素，肯定不是前K个最大数的一员
            else:
                heapq.heapreplace(self.minheap,val) # 把val值放进最小堆，让它重新调整顺序，便于以后区分
        else:
            heapq.heappush(self.minheap,val) # 前面k个元素直接放进最小堆
    
    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap

def test():
    import random
    i = list(range(100))
    random.shuffle(i) # 随机大乱这些值
    _ = TopK(i,10)
    print(_.get_topk())
test()