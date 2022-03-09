#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """使用pop实现 下一题用双指针实现"""
        l = len(nums)
        if l <= 1:
            return l
        i = 1
        while i <= l-1:
            if nums[i] == nums[i-1]:
                nums.pop(i)
                l -= 1
            else:
                i += 1
        return l

# @lc code=end

