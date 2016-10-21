# coding: utf8

'''

一个台阶总共有n 级，如果一次可以跳1 级，也可以跳2 级。

求总共有多少种跳法，并分析算法的时间复杂度。

'''


# use Cache, 事件复杂度: O(n)

def climb_stairs(n):
    result = [0, 1, 2]
    if n <= 2:
        return result[n]
    i = 3
    while i <= n:
        result.append(result[i - 1] + result[i - 2])
        i += 1
    return result[n]

# print(climb_stairs(10000))

'''
变形:

一个台阶总共有n 级，每次最大步数为 max (即每步可走1, 2, 3..., max)

求总共有多少种跳法

'''

def climb(n, max):
    sumStep = 0
    if n == 0:
        return 1
    if n >= max:
        for i in range(1, max + 1):
            sumStep += climb(n - i, max)
    else:
        sumStep += climb(n, n)
    return sumStep

print(climb(30, 3))


# witout Cache 使用递归, 效率低

