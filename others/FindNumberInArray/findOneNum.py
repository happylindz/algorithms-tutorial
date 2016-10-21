# coding:utf8

'''
题目：一个整型数组里除了一个数字之外，其他的数字都出现了两次。请写程序找出这那个只出现一次的数字。

时间复杂度 O(n)

空间复杂度 O(1)
'''

# 解题思路:
# 思路很简单, 直接使用异或运算即可求出, 即 result = a^b^b^c^c = a
# 如果数组中只有一个数出现一次, 其它数均出现两次, 那么可以直接使用异或运算求出单数, 因为重复的数在异或运算下为 0

def find_one_num(arr):
    result = 0
    for i in range(0, len(arr)):
        result ^= arr[i]
    return result

if __name__ == '__main__':
    print(find_one_num([1, 2, 3, 4, 5, 4, 3, 2, 1]))


# 补充:
# 异或运算其它用法(注: 异或运算满足交换律)

# 交换两个数而不占用新的空间
def swap(num1, num2):
    num1 ^= num2
    num2 ^= num1
    num1 ^= num2
    return (num1, num2)

# 判断两个数字是否相等

def equal(num1, num2):
    return (num1 ^ num2) == 0