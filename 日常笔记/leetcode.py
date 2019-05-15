# 1.给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
#   不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
# class Solution(object):
#     """
#     @param A: a list of integers
#     @return an integer
#     """
#     def removeDuplicates(self,A):
#         index = 0
#         while index < len(A)-1:
#             if A[index] == A[index+1]:
#                 del A[index+1]
#             else:
#                 index += 1
#             print(len(A))
#         return len(A)
# a = Solution()
# a.removeDuplicates([1,2,2,3,4,4,5])


# 2.给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

# [7,3,4,6,1,3,5,4,3,7,10]  思路：贪心算法，隔一天就比较，如果利润大于0，就交易;小于0，就不交易;最后算出总和  
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         index = 0
#         profits = 0  
#         for i in range(1,len(prices)):
#             money = prices[i] - prices[index]
#             if money > 0:
#                 # 买index索引值的股票
#                 profits += money
#                 index = i
#             else:
#                 index += 1
#         return profits
# a = Solution()
# print(a.maxProfit([7,3,4,6,1,3,5,4,3,7,10]))


# 3. 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。(写出三种方法)

# 示例 1:

# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]

# 思路1：当末尾的值加到前面的时候，改变之前每个值的索引 +1

# 第一种解法
# class Solution(object):
#     def rotate(self,nums,k):
#         '''向右旋转数组'''
#         for _ in range(k):
#             item = nums[-1]
#             for i in range(len(nums)-1,0,-1):
#                 nums[i] = nums[i-1]
#             nums[0] = item
#         return nums
# a = Solution()
# print(a.rotate([1,2,3,4,5,6,7,8,9,10],6))

# 第二种解法（切片）
# class Solution(object):
#     def rotate(self,nums,k):
#         '''向右旋转数组'''
#         nums = nums[-k:]+nums[:-k]
#         return nums
# a = Solution()
# print(a.rotate([1,2,3,4,5,6,7,8,9,10],6))

# 第三种解法(先反转，再交换顺序)
# class Solution(object):
#     def rotate(self,nums,k):
#         '''向右旋转数组'''
#         nums.reverse()
#         l1 = nums[:k]
#         l1.reverse()
#         l2 = nums[k:]
#         l2.reverse()
#         return l1 + l2
# print(Solution().rotate([1,2,3,4,5,6,7],3))

# 4.给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

# 示例 1:

# 输入: [1,2,3,1]
# 输出: true

# 算法1（不超时)
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         n1 = len(nums)
#         n2 = len(set(nums))
#         if n1 == n2:
#             return False
#         else:
#             return True

# 算法2（超时)
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         con = []
#         for num in nums:
#             if num not in con:
#                 con.append(num)
#             else:
#                 return True
#         return False



# 5.给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 示例 1:

# 输入: [2,2,1]
# 输出: 1

# 如果使用额外空间

# 算法1（使用异或)
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = 0
#         for i in range(len(nums)):
#             result ^= nums[i]
#         return result
# print(Solution().singleNumber([4,1,2,1,2]))




# class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         record, result = {}, []
#         for num in nums1:
#             record[num] = record.get(num, 0) + 1
                
#         for num in nums2:
#             if num in record and record[num]:
#                 result.append(num)
#                 record[num] -= 1
#         return result,record

# print(Solution().intersect([1,2,2,1],[2,2]))



# 6.给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。

# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         for i in range(len(digits)-1,-1,-1):
#             digits[i] += 1
#             if digits[i] == 10:
#                 digits[i] = 0
#                 continue
#             break
#         if digits[0] == 0:
#             digits[0] = 1
#             digits.append(0)
#         return digits



# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         ZeroNums = 0  # 0出现的次数
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 ZeroNums += 1
#             else:
#                 if ZeroNums != 0:
#                     nums[i-ZeroNums] = nums[i]
#                     nums[i] = 0
#                 else:
#                     continue
#         return nums

# print(Solution().moveZeroes([1,2,3,4,5]))



# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if nums[i] not in record:
                record[other] = i
            else:
                return [record[nums[i]],i]
print(Solution().twoSum([1,2,3,4,5],6))
        
            
        







