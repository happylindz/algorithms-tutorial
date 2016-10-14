# coding:utf8
import sys
import math


'''
LeetCode: https://leetcode.com/problems/perfect-squares/

279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

题目大意:

给一个正整数 n, 找出最少的数, 使得它们的平方和相加等于 n, 例如: n = 12, 12 = 4 + 4 + 4 则结果为 3

n = 13, 13 = 4 + 9 则结果为 2

'''

# 这题可以是使用动态规划进行计算, 初始化长度为 n + 1 的数组, 要求 n 的最少数, 要先求求出 n - i 前面的数, 通过前面的数去判断是最小数
# 法一, 法二均为动态规划的不同变形

def numSquares1(n):
    dp = [-1 for i in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        j = 1
        m = sys.maxint
        while j * j <= i:
            if j * j == i:
                m = 1
                break
            m = min(m, dp[i - j * j] + 1)
            j += 1
        dp[i] = m
    return dp[n]

# print(numSquares1(10234))

def numSquares2(n):
    dp = [sys.maxint for i in range(n + 1)]
    dp[0] = 0
    for i in range(0, n + 1):
        for j in range(1, int(math.sqrt(n - i)) + 1):
            if i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
    return dp[n]


# print(numSquares2(4))

# 法一, 法二显然不够高效, 下面有另外一种更高效一点的方法
# 法三: 需要用到一些定理:
# 1. 根据四平方和定理，任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，那么就是说返回结果只有1,2,3或4其中的一个
# 2. 由于一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等
# 3. 如果一个数除以8余7的话，那么肯定是由4个完全平方数组成
# 4. 尝试的将其拆为两个平方数之和，如果拆成功了那么就会返回1或2，因为其中一个平方数可能为0


def numSquares3(n):
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    a = 0
    while a * a <= n:
        b = int(math.sqrt(n - a * a))
        if a * a + b * b == n:
            if a != 0 and b != 0:
                return 2
            else:
                return 1
        a += 1
    return 3

# print(numSquares3(4341412414124))




