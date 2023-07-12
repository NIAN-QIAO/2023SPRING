from typing import List
'''
https://leetcode.cn/problems/battleships-in-a-board/
'''
'''
题目的关键问题在于重复计数，所以左或上存在X的格子不必计数，其它正常计数即可
'''


class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        num = 0
        for a in range(m):
            for b in range(n):
                # if board[a][b] == 'X':
                #     if a < 1 and b < 1:
                #         num += 1
                #     elif a < 1 and board[a][b - 1] != 'X':
                #         num += 1
                #     elif b < 1 and board[a - 1][b] != 'X':
                #         num += 1
                #     elif board[a - 1][b] != 'X' and board[a][b - 1] != 'X':
                #         num += 1
                # 丑陋的代码段
                if a > 0 and board[a - 1][b] == 'X':
                    continue
                if b > 0 and board[a][b - 1] == 'X':
                    continue
                if board[a][b] == 'X':
                    num += 1
        return num


if __name__ == '__main__':
    # board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    # board = [["."]]
    board = [["X", "X", "X"]]
    a = Solution()
    print(a.countBattleships(board))
