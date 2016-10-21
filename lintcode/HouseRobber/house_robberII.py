# coding: utf8

'''

LintCode: http://www.lintcode.com/zh-cn/problem/house-robber-ii/

534. 打劫房屋 II

在上次打劫完一条街道之后，窃贼又发现了一个新的可以打劫的地方，但这次所有的房子围成了一个圈，这就意味着第一间房子和最后一间房子是挨着的。

每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

样例

给出nums = [3,6,4], 返回　6，　你不能打劫3和4所在的房间，因为它们围成一个圈，是相邻的．

'''

# 与 houseRobber I 类似, 区别在于数组都头部和尾部不能同时被选中, 则我们可以将数组分割成为两个数组, 一个是不包含头部元素, 一个不包含尾部元素
# 分别代入 houseRoober I 中去计算, 最后在比较这个两个数的大小, 返回最大值


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


def houseRobber2(nums):
    # write your code here
    if len(nums)  == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        result1 = houseRobber(nums[:-1])
        result2 = houseRobber(nums[1:])
        return max(result1, result2)


if __name__ == '__main__':
    print(houseRobber2([3, 8, 4]))