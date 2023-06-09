from typing import List
'''
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。
示例 1:

输入: rowIndex = 3
输出: [1,3,3,1]
示例 2:

输入: rowIndex = 0
输出: [1]
示例 3:

输入: rowIndex = 1
输出: [1,1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        i = 0
        row = []
        while i <= rowIndex:
            j = 0
            element = []
            while j <= i:
                if j == 0 or j == i:
                    element.append(1)
                else:
                    element.append(row[i - 1][j - 1] + row[i - 1][j])
                j += 1
            row.append(element)
            i += 1
        return element


if __name__ == '__main__':
    a = Solution()
    print(a.getRow(3))
