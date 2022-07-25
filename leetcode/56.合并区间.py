#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List
# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])
        MAX = len(intervals)
        res = [intervals[0]]
        i = 1
        while i != MAX:
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
            i += 1
        return res

# @lc code=end


S = Solution()
print(S.merge(intervals=[[1, 4], [2, 3]]))
