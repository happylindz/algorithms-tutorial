# coding:utf8
from findTwoNum import find_two_numbers

'''
题目：一个整型数组里除了三个数字之外，其他的数字都出现了两次。请写程序找出这三个只出现一次的数字。

时间复杂度 O(n)

空间复杂度 O(1)
'''


# 解题思路:
# 跟前两个题目一样,如果我们能将数组的元素分成三堆, 每堆中的元素包含一个出现一次的数字以及其它若干的数字, 那么就回到最原始的问题
# 假设三个出现一次的数字为 x, y, z, 则对整个数组进行异或操作后 xors = x ^ y ^ z
# 这时候我们已经不能像找出两个数那样进行操作了, 通过观察我们可以发现 low_bit(x^y), low_bit(x^z), low_bit(y^z) 中有两个数是一样的, 另一个数是不一样的
# 简单证明下, 通过排除法, 如果三个数都一样,那么就会出现矛盾, 即出现某个位上 x 和 y 和 z 都不一样, 而某个位仅可能为0, 1. 所以显然不成立
# 如果三个数都不一样, 那就会出现比如 x^y = 001 x^z = 010 y^z = 100, 这显然也不行, 因为这与 x^y ^ x^z ^ y^z = 0 相互矛盾
# 所以 low_bit(x^y), low_bit(x^z), low_bit(y^z) 中有两个数是一样的, 另一个数是不一样的
# 那么我们设 flips = low_bit(x^y) ^ low_bit(x^z) ^ low_bit(y^z) = low_bit(x^y) 假设 low_bit(x^z) 和 low_bit(y^z) 一样
# 那么我们这时候只要再遍历一下数组, 找出 low_bit(xors ^ arr[i]) == flips, 这个数就是 x, 并且与 y, z 不会被选中, 被分离开了
# 最后从数组中删除这个元素, 然后再从数组中找到两个出现一次的数
# 时间复杂度: O(n)

def find_low_bit(num):
    index = 0
    while index < 32 and num & 1 == 0:
        num >>= 1
        index += 1
    return index

def judge_low_bit(num, index):
    num >>= index
    return (num & 1) != 0

def find_three_num(arr):
    xors = 0
    for i in range(0, len(arr)):
        xors ^= arr[i]

    flips = 0
    for i in range(0, len(arr)):
        flips ^= find_low_bit(xors ^ arr[i])

    num1 = 0
    for i in range(0, len(arr)):
        if find_low_bit(arr[i] ^ xors) == flips:
            num1 ^= arr[i]

    for i in range(0, len(arr)):
        if num1 == arr[i]:
            arr.pop(i)
            break
    return (num1,) + find_two_numbers(arr)

if __name__ == '__main__':
    print(find_three_num([1, 2, 3, 3, 4, 5, 4, 9, 9, 7, 7, 5, 8]))