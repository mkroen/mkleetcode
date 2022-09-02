#
# @lc app=leetcode.cn id=1906 lang=python3
#
# [1906] 查询差绝对值的最小值
#
from typing import List
# @lc code=start


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = [[0] * 101]
        for i in nums:
            s.append(s[-1].copy())
            s[-1][i] += 1
        res = []
        for a, b in queries:
            b += 1
            last = 0
            ans = -1
            for i in range(1,101):
                if s[b][i] == 0:
                    continue
                elif s[b][i]-s[a][i] == 0:
                    continue
                else:
                    if not last:
                        last = i
                    else:
                        ans = min(ans, i-last) if ans != -1 else i-last
                        last = i
            res.append(ans)
        return res
# @lc code=end

