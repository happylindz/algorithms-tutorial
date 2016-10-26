# coding: utf8

'''

LintCode: http://www.lintcode.com/zh-cn/problem/decode-ways/

512. 解码方法:
有一个消息包含A-Z通过以下规则编码

'A' -> 1
'B' -> 2
...
'Z' -> 26
现在给你一个加密过后的消息，问有几种解码的方式

样例

给你的消息为12，有两种方式解码 AB(12) 或者 L(12). 所以返回 2

'''

# 动态规划的题:
# 判断某个数 4534yx, 如果 x != 0, 则在 x 中至少有 dp[i - 1] 种情况,  dp[i] 表示从 0 ~ i 的位置组成的数有多少种情况
# 如果 x 前面的数 y 不为 0, 且 0 < yx <=26, 则dp[i] = dp[i - 1] + dp[i - 2]

def numDecodings(s):
    res = map(lambda x: int(x), list(str(s)))
    n = len(res)
    if n < 1:
        return 0
    elif n == 1:
        return 0 if res[0] == 0 else 1
    dp = [0 for i in range(n)]
    dp[0] = 1
    temp = res[0] * 10 + res[1]
    dp[1] = 2 if 0 < temp <= 26 and res[1] != 0 else 1
    for i in range(2, n):
        count = 0
        if res[i] != 0:
            count += dp[i - 1]
        temp = res[i - 1] * 10 + res[i]
        if 0 < temp <= 26 and res[i - 1] != 0:
            count += dp[i - 2]
        dp[i] = count
    return dp[n - 1]