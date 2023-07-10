from typing import List
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

 

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针？
        if len(nums) < 2:
            return
        after = len(nums) - 1
        while nums[after] == 0:
            after -= 1
            if after <= 0:
                return
        for before in range(after, -1, -1):
            # [ , )
            if nums[before] == 0:
                for k in range(before, after):
                    nums[k] = nums[k + 1]
                    # 填补
                nums[after] = 0
                after = after - 1
