# coding: utf8

'''

LintCode: http://www.lintcode.com/zh-cn/problem/paint-fence/

514. 栅栏染色

我们有一个栅栏，它有n个柱子，现在要给柱子染色，有k种颜色可以染。
必须保证最多只有两个相邻的柱子颜色不同，求有多少种染色方案。

样例:
n = 3, k = 2, return 6

      post 1,   post 2, post 3
way1    0         0       1
way2    0         1       0
way3    0         1       1
way4    1         0       0
way5    1         0       1
way6    1         1       0

'''

# 动态规划题:
# 如果 post i 与 post i - 1 柱颜色不同, 那么与 i - 2 柱颜色没关系
# 如果 post i 与 post i - 1 柱颜色相同, 那么它与 i - 2 柱颜色就一定得不同了
# 递推公式: dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)

def numWays(n, k):
    # Write your code here
    if n == 0 or (k == 1 and n >= 3):
        return 0
    elif n == 1:
        return k
    elif n == 2:
        return k * k
    dp = [0 for i in range(n)]
    dp[0] = k
    dp[1] = k * k
    for i in range(2, n):
        dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
    return dp[n - 1]