#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#
from typing import List
# @lc code=start


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m*n
        l = []
        kk = k
        for each in grid:
            if kk > n:
                l += each
                kk -= n
            else:
                l += each[:kk]
                break
        for i in range(m):
            for j in range(n):
                if k == 0:
                    l.append(grid[i][j])
                    grid[i][j] = l[0]
                    l = l[1:]
                else:
                    k -= 1
        for i in range(m):
            for j in range(n):
                if l:
                    grid[i][j] = l[0]
                    l = l[1:]
                else:
                    break
        return grid


# @lc code=end
S = Solution()
print(S.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))