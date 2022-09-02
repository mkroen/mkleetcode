#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#
from typing import List
# @lc code=start


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {a: i for i, a in enumerate(sorted(set(arr)), 1)}
        return [d[each] for each in arr]


# @lc code=end
S = Solution()
print(S.arrayRankTransform(arr=[100, 100, 100]))
