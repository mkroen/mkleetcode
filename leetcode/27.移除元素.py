#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """双指针"""
        i = 0
        f = 0
        l = len(nums)
        while f < l:
            if nums[f] != val:
                if i != f:
                    nums[i] = nums[f]
                i += 1
                f += 1
            else:
                f += 1
        return i

# @lc code=end

