# coding: utf8

'''

LintCode: http://www.lintcode.com/zh-cn/problem/house-robber/

392. 打劫房屋

假设你是一个专业的窃贼，准备沿着一条街打劫房屋。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且
当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

样例

给定 [3, 8, 4], 返回 8.

'''


# 这是一道动态规划的问题,  dp[i]表示从第 0 ~ 到 i 间所能产生的最大钱数, 那么dp[i] 则取决于 dp[i - 2] 或 dp[i -3] 的最大钱加上 A[i]
# 这样我们就定义了状态 dp[i] = max(dp[i - 2], dp[i - 3]) + A[i]
# 最后取 dp[n - 1]或 dp[n - 2] 的最大值


def houseRobber(A):
    # write your code here
    n = len(A)
    if n == 0:
        return 0
    elif n == 1:
        return A[0]
    elif n == 2:
        return max(A[0], A[1])
    else:
        dp = [-1 for i in range(n)]
        dp[0] = A[0]
        dp[1] = A[1]
        dp[2] = A[0] + A[2]
        for i in range(3, n):
            dp[i] = max(dp[i - 2], dp[i - 3]) + A[i]
        return max(dp[n - 1], dp[n - 2])
    

if __name__ == '__main__':
    print(houseRobber([3, 8, 4]))
