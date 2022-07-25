#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#
from typing import List

# @lc code=start


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(position)):
            if position[i] % 2 == 1:
                a += 1
            else:
                b += 1
        return min(a, b)

# @lc code=end
