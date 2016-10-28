# coding: utf8


'''

LintCode: http://www.lintcode.com/zh-cn/problem/longest-increasing-subsequence/

76. 最长上升子序列:
给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。

样例:

给出 [5,4,1,2,3]，LIS 是 [1,2,3]，返回 3

给出 [4,2,4,5,3,7]，LIS 是 [2,4,5,7]，返回 4

'''

def longestIncreasingSubsequence(nums):
    # write your code here
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    dp = [1 for i in range(n)]
    for i in range(1, n):
        max_sub = 1
        for j in range(i):
            if nums[i] > nums[j] and max_sub < dp[j] + 1:
                max_sub = dp[j] + 1
        dp[i] = max_sub
    return max(dp)
