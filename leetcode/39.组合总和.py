#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """排序，递归"""
        candidates.sort()
        res = []
        def find(c: List[int], t: int, last: List[int] = []):
            start, end = -1, len(c)
            for i in range(len(c)):
                if last:
                    if c[i] < last[-1]:
                        start = i
                if c[i] > t:
                    end = i
                    break
            c = c[start+1: end]
            for each in c:
                next_last = last.copy()
                next_last.append(each)
                if each == t:
                    res.append(next_last)
                else:
                    find(c, t-each, next_last)
        find(candidates,  target)
        return res


# @lc code=end

S = Solution()
candidates = [2]
target = 1
print(S.combinationSum(candidates, target))