from typing import List


class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        count = 0
        for i, element in enumerate(nums):
            if element == 1:
                count += 1
            else:
                max_num = max(count, max_num)
                count = 0
        max_num = max(count, max_num)
        return max_num
