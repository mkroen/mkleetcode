#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
from typing import List, Tuple
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """深度递归"""
        from copy import deepcopy
        def find_next(data: List[List[str]], last_col=0, last_row=0):
            for i in range(last_col, 9):
                for j in range(last_row if i==last_col else 0, 9):
                    if data[i][j] == ".":
                        return True, i, j
            return False, -1, -1
        
        def not_used(data: List[List[str]], col: int, row: int):
            not_use = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            for i in range(9):
                if data[col][i] in not_use:
                    not_use.remove(data[col][i])
                if data[i][row] in not_use:
                    not_use.remove(data[i][row])
            for i in range(3):
                for j in range(3):
                    if data[col//3*3+i][row//3*3+j] in not_use:
                        not_use.remove(data[col//3*3+i][row//3*3+j])
            return tuple(not_use)
        
        def solve(data: List[List[str]], last_col=0, last_row=0):
            has_next, col, row = find_next(data, last_col, last_row) 
            if not has_next:
                for i in range(9):
                    for j in range(9):
                        board[i][j] = data[i][j]
                return
            else:
                not_use = not_used(data, col, row)
                if not not_use:
                    return
                else:
                    for each in not_use:
                        next_data = deepcopy(data)
                        next_data[col][row] = each
                        solve(next_data, col, row)
        solve(deepcopy(board))

# @lc code=end
S = Solution()
board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
S.solveSudoku(board)
print(board)
