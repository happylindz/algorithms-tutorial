# coding:utf8

'''
LeetCode: https://leetcode.com/problems/two-sum/

1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

题目大意:
给定一个数组和一个数, 在数组中寻找两个数, 判断两数之和是否为该特定的数, 如果是, 则返回这两个数的索引值

'''


# 解题思路:
# 刚看到这个题, 第一反应想到的方法可能就是暴力破解法, 套一个二重循环, 比较数组中任意两个数之和是否为 target 值
# 时间复杂度: O(n^2)

def two_sum1(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None

# print(two_sum1([1, 2, 3, 4, 5, 6], 7))

# 该方法简单直观, 但是效率太低, 那么有什么方法可以进行优化
# 我们先将数组进行排序,然后从头部和尾部分别进行遍历, 直到找到答案为止,
# 时间复杂度: O(nlogn)(快排) + O(n)(遍历数组) + O(2n)(找到索引) = O(nlogn)


def quick_sort(arr, left, right):
    count = 0
    if left >= right:
        return arr
    item = arr[left]
    i, j = left, left + 1
    while j <= right:
        count += 1
        if arr[j] < item:
            arr[j], arr[i + 1] = arr[i + 1], arr[j]
            i += 1
        j += 1
    arr[left], arr[i] = arr[i], arr[left]
    quick_sort(arr, left, i - 1)
    quick_sort(arr, i + 1, right)
    return arr


def two_sum2(arr, target):
    new_arr = arr
    quick_sort(new_arr, 0, len(arr) - 1)
    left, right = 0, len(new_arr) - 1
    while left < right:
        if new_arr[left] + new_arr[right] == target:
            break
        elif new_arr[left] + new_arr[right] < target:
            left += 1
        else:
            right -= 1
    for i in range(len(arr)):
        if new_arr[left] == arr[i]:
            left = i
            break
    for i in range(len(arr)):
        if new_arr[right] == arr[i]:
            right = i
            break
    if left == right:
        return []
    return [left, right]

# print(two_sum2([1, 2, 3, 4, 5, 6], 7))

# 方法2 虽然效率提升了, 又要花费更多的空间, 也不是太好
# 方法三的思路是将数组的信息存在一个 hash 表里, 用数组的值作为 key, 索引作为 value
# 用 key 去查找是否有匹配项
# 时间复杂度: O(n)

def two_sum3(arr, target):
    res = dict()
    n = len(arr)
    for i in range(n):
        res[arr[i]] = i
    for i in range(n):
        num = target - arr[i]
        if num in res:
            if res[num] == i:
                continue
            elif res[num] < i:
                return [res[num], i]
            else:
                return [i, res[num]]
    return []

print(two_sum3([1, 2, 3, 4, 5, 6], 7))
