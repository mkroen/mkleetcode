#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """基数排序思想"""
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                continue
            if nums[i] != i+1:
                while True:
                    if nums[i] <= length:
                        if nums[i] == nums[nums[i]-1]:
                            break
                        index = nums[i]-1
                        nums[i], nums[index] = nums[index], nums[i]
                    else:
                        break
                    if nums[i] <=0 or nums[i] == i+1:
                        break
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length+1
# @lc code=end

S = Solution()
nums = []
print(S.firstMissingPositive(nums))