from typing import List


class Solution:

    def findPoisonedDuration(self, timeSeries: List[int],
                             duration: int) -> int:
        res = begin = end = 0
        for i, element in enumerate(timeSeries):
            if i == 0:
                begin = element
                end = begin + duration - 1
            else:
                if element > end:
                    res += duration
                else:
                    res += element - begin
                begin = element
                end = begin + duration - 1
        res += end - begin + 1
        return res


timeSeries = [1, 4]
duration = 2
a = Solution()
res = a.findPoisonedDuration(timeSeries, duration)
print(res)
