from typing import List


# 列表取三个乘积最大值，要么是三个正数最大值，要么是两个负数最小值和一个正数最大值
class Solution:

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for temp in nums:
            if temp < 0:
                count += 1
            if count > 1:
                break
        if count > 1:
            return max(
                nums[0] * nums[1] * nums[len(nums) - 1], nums[len(nums) - 1] *
                nums[len(nums) - 2] * nums[len(nums) - 3])
        else:
            return nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) -
                                                                    3]
