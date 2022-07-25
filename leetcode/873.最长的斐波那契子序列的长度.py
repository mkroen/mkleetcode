#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#
from typing import List
# @lc code=start


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # dfs卡着过，应该能剪枝
        # return res=2的时候 wa了一发 应该return 0
        s = set(arr)
        res = 0

        def dfs(last: List[int], count: int):
            nonlocal s, res
            if sum(last) in s:
                dfs([last[-1], sum(last)], count+1)
            else:
                res = max(res, count)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                dfs([arr[i], arr[j]], 2)
        return res if res > 2 else 0
# @lc code=end
