# coding: utf8

'''
LintCode: http://www.lintcode.com/zh-cn/problem/3sum-closest/

59. 最接近的三数之和:

给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和。

注意事项:
只需要返回三元组之和，无需返回三元组本身

样例:
例如 S = [-1, 2, 1, -4] and target = 1. 和最接近 1 的三元组是 -1 + 2 + 1 = 2.
'''

# 题目与上面的类似, 同样先排序, 然后再找答案


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        n = len(numbers)
        if n < 3:
            return []
        nums = self.quick_sort(numbers, 0, n - 1)
        i, result = 0, 0
        diff = sys.maxint
        while i < n - 1:
            item = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                left, right = nums[j], nums[k]
                sum = item + left + right
                if sum == target:
                    return target
                elif sum < target:
                    if diff > target - sum:
                        result = sum
                        diff = target - sum
                    j += 1
                else:
                    if diff > sum - target:
                        result = sum
                        diff = sum - target
                    k -= 1
            i += 1
        return result

    def quick_sort(self, nums, left, right):
        if left >= right:
            return nums
        key = nums[left]
        lp, rp = left, right
        while lp < rp:
            while lp < rp and nums[rp] >= key:
                rp -= 1
            while lp < rp and nums[lp] <= key:
                lp += 1
            nums[lp], nums[rp] = nums[rp], nums[lp]
        nums[lp], nums[left] = nums[left], nums[lp]
        self.quick_sort(nums, left, lp - 1)
        self.quick_sort(nums, rp + 1, right)
        return nums