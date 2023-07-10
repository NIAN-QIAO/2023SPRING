from typing import List
'''
给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

'''
'''
贪心算法

本题是要维持一个非递减的数列，所以遇到递减的情况时（nums[i] > nums[i + 1]），要么将前面的元素缩小，要么将后面的元素放大。

但是本题唯一的易错点就在这，

如果将nums[i]缩小，可能会导致其无法融入前面已经遍历过的非递减子数列；
如果将nums[i + 1]放大，可能会导致其后续的继续出现递减；
所以要采取贪心的策略，在遍历时，每次需要看连续的三个元素，也就是瞻前顾后，遵循以下两个原则：

需要尽可能不放大nums[i + 1]，这样会让后续非递减更困难；
如果缩小nums[i]，但不破坏前面的子序列的非递减性；
算法步骤：

遍历数组，如果遇到递减：
还能修改：
修改方案1：将nums[i]缩小至nums[i + 1]；
修改方案2：将nums[i + 1]放大至nums[i]；
不能修改了：直接返回false；
'''


class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        flag = True
        if len(nums) < 2:
            # 只有一个数
            return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # if flag == False:
                if not flag:
                    return flag
                if i == 0:
                    # 如果刚开始就递减
                    nums[i] = nums[i + 1]
                    flag = False
                else:
                    if nums[i + 1] >= nums[i - 1]:
                        nums[i] = nums[i + 1]
                    else:
                        nums[i + 1] = nums[i]
                    flag = False
        return True


if __name__ == '__main__':
    nums = [4, 2, 3]
    a = Solution()
    print(a.checkPossibility(nums))
