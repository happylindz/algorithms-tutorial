'''
LintCode: http://www.lintcode.com/zh-cn/problem/find-minimum-in-rotated-sorted-array/

159. 寻找旋转排序数组中的最小值：

假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

你可以假设数组中不存在重复的元素。

样例

给出[4,5,6,7,0,1,2]  返回 0
'''

# 二分查找法： 
# 假如翻转后的数组以第 x 个结点分为两部分 A[0..x] 和 A[x+1..n]。则 A[0..x] 这一段是有序递增的， 
# A[x+1..n] 这一段也是有序递增的。并且因为原数组是有序递增的，
# A[0..x] 中所有数都会大于 A[x+1..n] 中的任何数。所以我们其实就是需要找到结点 A[x+1]，这个结点的值就是最小值。
# 考虑数组 A[i..j]，中间结点 m （m = (i + j ) / 2)。
# A[i] < A[j]：数组是递增的，说明已经找到 x 结点，并且 x 等于 i。
# A[i] >= A[j]：数组不是递增的，说明 x 结点还没有找到，这时对比中间结点 A[m]
# A[m] > A[i]： 则数组中 A[i..m] 这一段是有序递增的，翻转结点 x 定不会在这一段中，这时我们只需要考虑 A[m+1..j] 这一段。
# A[m] < A[i]：说明翻转结点 x 在 A[i..m]中。


class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        n = len(nums)
        if n < 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) / 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else: 
                right = mid
        return nums[left]