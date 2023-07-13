from typing import List
'''
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
'''


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 普通版本
        # k = k % len(nums)
        # temp = [nums[a] for a in range(len(nums) - k, len(nums))]
        # # [)
        # for i in range(len(nums) - k - 1, -1, -1):
        #     nums[i + k] = nums[i]
        # for a in range(0, k):
        #     nums[a] = temp[a]
        # return
        # 数组翻转版本
        n = len(nums)
        k %= n
        # 翻转整个数组
        self.reverse(nums, 0, n - 1)
        # 翻转前k个元素
        self.reverse(nums, 0, k - 1)
        # 翻转k后面个元素
        self.reverse(nums, k, n - 1)

    # 双指针颠倒
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
