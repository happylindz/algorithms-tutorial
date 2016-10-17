# coding:utf8

'''
leetCode: https://leetcode.com/problems/missing-number/
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

题目大意:
题目大意是，给定一个包含从0, 1, 2, ..., n, 选出的n个不同数字的数组，从中找出数组中缺失的那一个数。

'''

# 法一: 构造一个等差数列求和的值sum(从 0 ~ n)
# 遍历整个数组,  用sum去扣除每个数, 则最后剩下的 sum 值即为缺失的值

def missingNumber1(nums):
    n = len(nums)
    sum = (1 + n) * n / 2
    for i in range(n):
        sum -= nums[i]
    return sum

# 法二: 使用异或运算符, 我们都知道: x = a ^ a = 0
# 则一开始令 x = 1^2^...^n
# 然后再与数组每一项进行异或运算, 所有成对的数字都被抵消, 则出现一次的即为所求的缺失数

def missingNumber2(nums):
    n = len(nums)
    sum = 0
    for i in range(n + 1):
        sum ^= i
    for i in range(n):
        sum ^= nums[i]
    return sum

if __name__ == '__main__':
    print missingNumber1([0, 3, 2, 1, 4, 8, 6, 7])
    print missingNumber2([0, 3, 2, 1, 4, 8, 6, 7])
