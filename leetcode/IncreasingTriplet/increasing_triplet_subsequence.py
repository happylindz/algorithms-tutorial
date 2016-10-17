# coding: utf8
import sys
'''
LeetCode: https://leetcode.com/problems/increasing-triplet-subsequence/

334. Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

题目大意:

题目大意是，给定一个无序数组，判断其中是否存在一个长度为3的递增子序列。

即是，如果存在下标i, j, k(0 ≤ i < j < k ≤ n-1)，使得arr[i] < arr[j] < arr[k]，返回true，否则返回false。

要求满足O(n)的时间复杂度和O(1)的空间复杂度。 (i, j, k 不一定要是连续的)

'''

# 要求只要在数组中找到三个递增的元素即可，不要求这三个元素是否连续，
# 因此，只需维护两个整数变量 first, second，用来记录数组中大小递增的前2个元素，满足条件时，应该有：first < second < nums[i]

def increasing_triplet(nums):
    n = len(nums)
    if n < 3:
        return False
    first, second = sys.maxint, sys.maxint
    for i in range(n):
        if nums[i] <= first:
            first = nums[i]
        elif nums[i] <= second:
            second = nums[i]
        else:
            return True
    return False

if __name__ == '__main__':
    print(increasing_triplet([1, 8, 6, 3, 4, 5]))