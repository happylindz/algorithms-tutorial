# coding: utf8

def canJump(nums):
    i, maxStep = 1, nums[0]
    n = len(nums)
    while i < n:
        if maxStep == 0:
            return False
        maxStep -= 1
        if maxStep < nums[i]:
            maxStep = nums[i]
        if maxStep + i >= n:
            return True
        i += 1
    return True


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
