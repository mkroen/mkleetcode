#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#
from typing import List
# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        m_l = [0]*m
        n_l = [0]*n
        for a,b in indices:
            m_l[a]+=1
            n_l[b]+=1
        res = 0
        for i in range(m):
            for j in range(n):
                res += (m_l[i] + n_l[j])%2
        return res

# @lc code=end

S = Solution()
print(S.oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))
