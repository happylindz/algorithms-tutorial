# coding: utf8

'''
LeetCode: 229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run
in linear time and in O(1) space.

题目大意:
给定一个大小为 n 的数组, 找某种特定的元素, 这种元素满足在这个数组至少出现 n / 2 次

'''


# 解题思路:
# 跟 169. Majority Element 差不多


class Solution(object):
    @staticmethod
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums
        num1, num2, time1, time2 = None, None, 0, 0
        n = len(nums)
        for i in range(0, n):
            if num1 == nums[i]:
                time1 += 1
            elif num2 == nums[i]:
                time2 += 1
            elif time1 == 0:
                num1 = nums[i]
                time1 = 1
            elif time2 == 0:
                num2 = nums[i]
                time2 = 1
            else:
                time1 -= 1
                time2 -= 1
        time1 = 0
        time2 = 0
        for i in range(0, n):
            if nums[i] == num1:
                time1 += 1
            elif nums[i] == num2:
                time2 += 1
        result = []
        if time1 > n / 3:
            result.append(num1)

        if time2 > n / 3:
            result.append(num2)
        return result


    
if __name__ == '__main__':
    print(Solution.majorityElement([1, 2, 3, 4, 5, 1, 2, 1, 2, 2, 1, 1, 2, 2]))