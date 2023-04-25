from typing import List
# from collections import Counter


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        # 对于一个长度为n的数组，其中没有出现的最小正整数只能在[1,n+1]中
        n = len(nums)
        for i in range(n):
            if nums[i] >= n + 1 or nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = nums[i]
            if 1 <= abs(num) <= n and nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = -nums[abs(num) - 1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
