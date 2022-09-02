#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#
from typing import List
# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        if Counter(target) == Counter(arr):
            return True
        return False
# @lc code=end

S = Solution()
print(S.canBeEqual(target = [3,7,9], arr = [3,7,11]))