from typing import List
# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
'''
输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

输入：nums = [1,1,1]
输出：0
'''
'''
假设最小的变化次数为k
则变化后的数列和为 sum(nums)+k*(n-1)
变化后每个数为target,数列总和为 n*target
关键问题在于知道target的值
target就是min(nums)+k
sum(nums)+k*(n-1)=n*target
sum(nums)+k*(n-1)=n*(min(nums)+k)
k=sum(nums)-n*min(nums)
'''


class Solution:

    def minMoves(self, nums: List[int]) -> int:
        # return sum(nums) - len(nums) * min(nums) if len(nums) != 1 else 0
        if len(nums) != 1:
            return sum(nums) - len(nums) * min(nums)
        else:
            return 0


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    a = Solution()
    print(a.minMoves(nums))
