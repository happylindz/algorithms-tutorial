# coding: utf8

'''

LintCode: http://www.lintcode.com/zh-cn/problem/backpack/

92.背包问题:

在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

注意事项:

你不可以将物品进行切割。

样例:

如果有4个物品[2, 3, 5, 7]

如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。

如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。

函数需要返回最多能装满的空间大小。

'''

# 法一: 动态规划
# 状态: res[i][S] 表示前i个物品，取出一些物品能否组成体积和为S的背包
# 状态转移方程: f[i][S]=f[i−1][S−A[i]] or f[i−1][S]
# 欲从前i个物品中取出一些组成体积和为S的背包，可从两个状态转换得到。
# f[i−1][S−A[i]]: 放入第i个物品，前 i−1 个物品能否取出一些体积和为 S−A[i] 的背包。
# f[i−1][S]: 不放入第i个物品，前 i−1 个物品能否取出一些组成体积和为S的背包。
# 状态初始化: f[1⋯n][0]=true; f[0][1⋯m]=false. 前1~n个物品组成体积和为0的背包始终为真，其他情况为假。
# 返回结果: 寻找使 f[n][S] 值为true的最大S (1≤S≤m)


def backPack1(m, A):
    # write your code here
    lenA = len(A)
    if m < 1 or lenA == 0:
        return 0
    res = [[False for i in range(m + 1)] for j in range(lenA + 1)]
    res[0][0] = True
    for i in range(1, lenA + 1):
        for j in range(m + 1):
            if j < A[i - 1]:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = res[i - 1][j] or res[i - 1][j - A[i - 1]]
    for i in range(m, -1, -1):
        if res[lenA][i] == True:
            return i

# 每次 res[i][j] 都会一来到 res[i - 1][j] 的结果, 那么如果仅仅使用一维数组的话, 那么我们每次在添加一个商品的时候,我们倒序遍历这个数组,
# 保证每次 res[i] 都能用到上次的 res[i]


def backPack2(m, A):
    # write your code here
    lenA = len(A)
    if m < 1 or lenA == 0:
        return 0
    res = [False for i in range(m + 1)]
    res[0] = True
    for i in range(lenA):
        for j in range(m, 0, -1):
            if j >= A[i] and res[j - A[i]]:
                res[j] = True
    for i in range(m, -1, -1):
        if res[i] == True:
            return i
