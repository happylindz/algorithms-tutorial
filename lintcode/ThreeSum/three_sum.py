# coding: utf8


'''

LintCode: http://www.lintcode.com/zh-cn/problem/3sum/

57. 三数之和:

给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

注意事项:
在三元组(a, b, c)，要求a <= b <= c。
结果不能包含重复的三元组。

样例
如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：
(-1, 0, 1)
(-1, -1, 2)

'''

# 解题思路:
# 先将数组从小到大进行排序, 这里我们使用快速排序, 然后指定 i 遍历数组, 假定 i 为三个数其中之一, 然后设置两个指针 j = i + 1, k = 数组尾元素
# 判断 nums[i] + nums[j] + nums[k] 与 0 进行比较, 如果大了就把尾指针 k--, 小了则头指针 j++
# 相等则将结果添加到结果集, 为了避免重复添加, 需要加入一些判断来排除重复的结果被添加
# 时间复杂度: O(nlogn) + O(m) = O(nlogn)

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        n = len(numbers)
        if n < 3:
            return []
        nums = self.quick_sort(numbers, 0, n - 1)
        i, result = 0, []
        while i < n - 1:
            item = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if item + nums[j] + nums[k] == 0:
                    result.append((item, nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j, k= j + 1, k - 1
                elif item + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
            while item == nums[i] and i < n - 1:
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
