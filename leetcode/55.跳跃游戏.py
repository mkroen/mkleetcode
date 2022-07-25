#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List
# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 循环一遍，求最远距离，复杂度On，但似乎比找0慢？
        l = 0
        for i, n in enumerate(nums):
            if i > l:
                return False
            l = max(l, i+nums[i])
        return True

    def canJump_v3(self, nums: List[int]) -> bool:
        # 找0，看能不能跳过0 复杂度On2，还能优化
        last = -1
        flag = False
        for i, n in enumerate(nums[:-1]):
            if n == 0:
                flag = True
                for j in range(last+1, i):
                    if j+nums[j] > i:
                        flag = False
                        break
                if flag:
                    return False
        return True

    def canJump_v2(self, nums: List[int]) -> bool:
        # dfs能过，但太慢了，几乎卡着过的
        flag = False
        aim = len(nums) - 1
        tried = set()

        def dfs(index):
            nonlocal flag, aim, tried
            if not flag:
                if index+nums[index] >= aim:
                    flag = True
                    return
                for i in range(1, nums[index]+1):
                    if i+index not in tried:
                        tried.add(i+index)
                        dfs(i+index)
        dfs(0)
        return flag
# @lc code=end
