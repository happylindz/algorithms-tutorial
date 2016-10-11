# coding:utf8

'''
LeetCode: 169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

题目大意:
给定一个大小为 n 的数组, 找一个特定的元素, 这个元素满足在这个数组至少出现 n / 2 次, 你可以假设数组非空, 并且这个元素是真实存在的
'''


# 解题思路:
# 可以成对地排除那些不相等的元素, 直到剩下最后一个元素.
# 因为这个元素一定是存在的并且多于占数组元素的一半, 那么我们可以指定一个 count 和 selectedItem,
# 一开始可以令第一个元素为 selectedItem, 并且 count += 1, 如果下个元素不是 selectedItem, 则将 count -= 1, 否则 count += 1
# 如果 count == 0 的话就重新指定下一个元素为 selectedItem, 并且 count 置为 1, 不管新值与旧值是否相等
# 这样最后剩下来的元素就是所求元素
# 时间复杂度: O(n)  空间复杂度: O(1)


class Solution(object):
    @staticmethod
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        selected_item = None
        count = 0
        for i in range(0, len(nums)):
            if count == 0:
                selected_item = nums[i]
                count += 1
            else:
                if selected_item == nums[i]:
                    count += 1
                else:
                    count -= 1
        return selected_item


if __name__ == '__main__':
    print(Solution.majorityElement(None, [2, 1, 4, 1, 6, 1, 7, 1, 8, 1, 1]))


# 因为这里明确该数组中必包含主元素, 所以我们前面的代码才成立, 如果去掉假设 (数组非空, 并且这个元素是真实存在的)
# 考虑数组为: [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1] 最后输出还是为 1,而实际 1 并不是主元素
# 如果去掉假设的话, 可以使用一个字典来存储元素的 key 和出现的次数来遍历整个数组
# 最后查看字典中是否有元素的 value 大于 len(arr) / 2
# 时间复杂度: O(n)

def find_majority_element1(nums):
    if len(nums) == 0:
        return None
    elems = dict()
    n = len(nums)
    for i in range(0, n):
        if nums[i] in elems.keys():
            elems[nums[i]] += 1
        else:
            elems[nums[i]] = 1
    for k, v in elems.iteritems():
        if v > n / 2:
            return k
    return None


# 或者修改下之前的代码:
def find_majority_element2(nums):
    if len(nums) == 0:
        return None
    selected_item = None
    count = 0
    for i in range(0, len(nums)):
        if count == 0:
            selected_item = nums[i]
            count += 1
        else:
            if selected_item == nums[i]:
                count += 1
            else:
                count -= 1
    count = 0
    for i in range(0, len(nums)):
        if selected_item == nums[i]:
            count += 1
    if count >= len(nums) / 2:
        return selected_item

# print(find_majority_element1([1, 2, 3, 5, 1, 1, 1, 1, 1, 1]))
# print(find_majority_element2([1, 2, 3, 5, 1, 1, 1, 1, 1, 1]))


