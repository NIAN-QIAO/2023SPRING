from typing import List
'''
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        row = []
        while i < numRows:
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
        return row
