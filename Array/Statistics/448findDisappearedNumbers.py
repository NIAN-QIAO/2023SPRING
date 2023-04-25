from typing import List
from collections import Counter


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        res = []
        for i in range(1, len(nums) + 1):
            tmp = dic.get(i, 0)
            if tmp == 0:
                res.append(i)
        return res
