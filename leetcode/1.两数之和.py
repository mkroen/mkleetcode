#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            num_2 = target - num
            if num_2 in hashmap:
                return [hashmap[num_2], index]
            hashmap[num] = index
        return []
# @lc code=end

