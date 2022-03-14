#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """类似上一题，排序，递归，递归时记得去重"""
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
            num = None
            for i in range(len(c)):
                if c[i] == num:
                    continue
                else:
                    num = c[i]
                next_last = last.copy()
                next_last.append(c[i])
                if c[i] == t:
                    res.append(next_last)
                else:
                    find(c[i+1:], t-c[i], next_last)
        find(candidates, target)
        return res
# @lc code=end

S = Solution()
candidates = [2,5,2,1,2]
target = 5
print(S.combinationSum2(candidates, target))