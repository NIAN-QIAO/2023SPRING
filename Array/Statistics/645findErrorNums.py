from typing import List
from collections import Counter


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeat = loss = 0
        dic = Counter(nums)
        # 查找字典 dic 中是否存在键值为 i 的元素，如果存在，则返回对应的值；如果不存在，则返回默认值 0
        for i in range(1, len(nums) + 1):
            tmp = dic.get(i, 0)
            if tmp == 0:
                loss = i
            if tmp == 2:
                repeat = i
        return [repeat, loss]

    def findErrorNums1(self, nums: List[int]) -> List[int]:
        repeat = sum(nums) - sum(set(nums))
        loss = sum(range(len(nums) + 1)) - sum(set(nums))
        return [repeat, loss]
