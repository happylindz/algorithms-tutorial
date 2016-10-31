'''
LintCode: http://www.lintcode.com/zh-cn/problem/find-minimum-in-rotated-sorted-array-ii/

160. 寻找旋转排序数组中的最小值 II

假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

数组中可能存在重复的元素。

样例：

给出[4,4,5,6,7,0,1,2]  返回 0
'''

# 跟 findMin I 类似
# 因为可能存在重复的元素，所以在判断 num[left] >= num[mid] 之后
# 需要判断 left - mid 之间的元素是否相等，如果相等，那就说明最小元素在后半段
# 如果不相等，则说明最小元素在前半段

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        n = len(num)
        if n < 1:
            return 0
        left = 0
        right = n - 1
        while left < right:
            if num[left] < num[right]:
                return num[left]       
            mid = (left + right) / 2
            if num[left] < num[mid]:
                left = mid + 1
            else:
                flag = True
                for i in range(left, mid + 1):
                    if num[left] != num[i]:
                        right = mid
                        flag = False
                if flag:
                    left = mid + 1
                
        return num[left]