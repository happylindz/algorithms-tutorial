# coding: utf8


'''

LintCode: http://www.lintcode.com/zh-cn/problem/backpack-ii/

125. 背包问题 II:

给出n个物品的体积A[i]和其价值V[i]，将他们装入一个大小为m的背包，最多能装入的总价值有多大？

注意事项:

A[i], V[i], n, m均为整数。你不能将物品进行切分。你所挑选的物品总体积需要小于等于给定的m。

样例:

对于物品体积[2, 3, 5, 7]和对应的价值[1, 5, 2, 4], 假设背包大小为10的话，最大能够装入的价值为9。

'''


# 法一: 二维数组 & 动态规划

def backPackII1(m, A, V):
    # write your code here
    lenA = len(A)
    lenV = len(V)
    if lenA == 0 or lenV == 0 or m <= 0:
        return 0
    res = [[0 for j in range(m + 1)] for i in range(lenA + 1)]
    for i in range(1, lenA + 1):
        for j in range(0, m + 1):
            if j < A[i - 1]:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - A[i - 1]] + V[i - 1])
    return res[lenA][m]


print(backPackII1(100, [77, 22, 29, 50, 99], [92, 22, 87, 46, 90]))


# 法二: 一维数组 & 动态规划

def backPackII2(m, A, V):
    # write your code here
    lenA = len(A)
    lenV = len(V)
    if m <= 0 or lenA == 0 or lenV == 0:
        return 0
    res = [0 for i in range(m + 1)]
    for i in range(lenA):
        for j in range(m, 0, -1):
            if j >= A[i]:
                temp = res[j - A[i]] + V[i]
                res[j] = max(res[j], temp)
    return res[m]


print(backPackII2(100, [77, 22, 29, 50, 99], [92, 22, 87, 46, 90]))
