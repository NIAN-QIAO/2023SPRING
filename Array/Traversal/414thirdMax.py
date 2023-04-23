from typing import List


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_num = temp = nums[0]
        count = 0
        for i, element in enumerate(nums):
            if element < temp and count < 2:
                temp = element
                count += 1
            if count == 2:
                return temp
        return max_num


# 维护前三大的数字
