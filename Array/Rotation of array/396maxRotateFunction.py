from typing import List
'''
给定一个长度为 n 的整数数组 nums 。
假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
返回 F(0), F(1), ..., F(n-1)中的最大值 。
生成的测试用例让答案符合 32 位 整数。
示例 1:
输入: nums = [4,3,2,6]
输出: 26
解释:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
示例 2:
输入: nums = [100]
输出: 0
'''


class Solution:
    '''
    # 使用前面189的结论，超时代码段
    # def reverse(self, nums: List[int], start: int, end: int) -> None:
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1

    # def rotate(self, nums: List[int], k: int) -> None:

    #     n = len(nums)
    #     k %= n
    #     self.reverse(nums, 0, n - 1)
    #     self.reverse(nums, 0, k - 1)
    #     self.reverse(nums, k, n - 1)
    #     return

    # def F(self, nums: List[int]) -> int:
    #     length, total = len(nums), 0
    #     for i in range(length):
    #         total = i * nums[i] + total
    #     return total

    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     max_number = self.F(nums)
    #     for i in range(len(nums) - 1):
    #         self.rotate(nums, 1)
    #         result = self.F(nums)
    #         if result > max_number:
    #             max_number = result
    #     return max_number
    '''
    '''
    记数组 nums的元素之和为 numSum
    根据公式，可以得到
    当1<=k<n时,F(k)=F(k-1)+numSum-n*nums[n-k]
    迭代计算
    '''

    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res


if __name__ == '__main__':
    example = Solution()
    nums = [4, 3, 2, 6]
    print(example.maxRotateFunction(nums))