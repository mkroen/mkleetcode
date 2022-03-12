#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from typing import List
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        横竖分别用一个map存
        九宫格用List[set]存
        """
        map = [set() for _ in range(9)]
        for i in range(9):
            col = set()
            row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in col:
                        return False
                    else:
                        col.add(board[i][j])
                    index = i//3 + j//3 * 3
                    if board[i][j] in map[index]:
                        return False
                    else:
                        map[index].add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in row:
                        return False
                    else:
                        row.add(board[j][i])
        return True
                

# @lc code=end
S = Solution()
board = [
[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]

print(S.isValidSudoku(board))
