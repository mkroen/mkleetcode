#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#
from typing import List
# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total, count = 0, 0
        l = len(nums)
        for i, n in enumerate(nums):
            total += i*n
            count += n
        max_total = total
        for n in nums[::-1]:
            total = total + count - n*l
            max_total = max(max_total, total)
        return max_total

# @lc code=end

S = Solution()
nums = []
print(S.maxRotateFunction(nums))