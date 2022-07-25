#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(l: List[int], nums: List[int]):
            if not nums:
                nonlocal res
                res.append(l)
                return
            for i in range(len(nums)):
                dfs(l+[nums[i]], nums[0:i]+nums[i+1:])
        dfs([],nums)
        return res

# @lc code=end
