# coding: utf8

'''

奇偶调序:

输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。要求时间复杂度为O(n)。

'''


# 设置头尾两个指针, 分别从前往后和从后往前遍历数组, 当遇到头指针为偶数, 尾指针为奇数时交换它们

def odd_even_sort1(nums):
    n = len(nums)
    if n <= 1:
        return nums
    left, right = 0, n - 1
    while left < right:
        while nums[left] & 1 == 1:
            left += 1
        while nums[right] & 1 == 0:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


# 维护两个指针i和j，一个指针指向数组的第一个数的前一个位置，我们称之为后指针i，向右移动；一个指针指向数组第一个数，称之为前指针j，也向右移动，
# 且前指针j先向右移动。如果前指针j指向的数字是奇数，则令i指针向右移动一位，然后交换i和j指针所各自指向的数字。

def odd_even_sort2(nums):
    n = len(nums)
    if n <= 1:
        return nums
    front, latter = -1, 0
    while latter < n:
        if nums[latter] & 1 == 1:
            front += 1
            nums[front], nums[latter] = nums[latter], nums[front]
        latter += 1
    return nums


if __name__ == '__main__':
    print(odd_even_sort1([2, 44, 3, 6, 87, 1, 3, 5]))
    print(odd_even_sort2([2, 44, 3, 6, 87, 1, 3, 5]))

'''
举一反三:

一个未排序整数数组，有正负数，重新排列使负数排在正数前面，并且要求不改变原来的正负数之间相对顺序.

比如： input: 1,7,-5,9,-12,15 ans: -5,-12,1,7,9,15 要求时间复杂度O(n),空间O(1)。
'''

# 详见: http://blog.csdn.net/v_july_v/article/details/7329314