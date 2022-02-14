from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int: # type: ignore
        l = [False for _ in nums]
        for num in nums:
            if not l[num]:
                l[num] = True
            else:
                return num

# 执行用时：36 ms, 在所有 Python3 提交中击败了91.86%的用户
# 内存消耗：23.6 MB, 在所有 Python3 提交中击败了29.65%的用户
# 通过测试用例：25 / 25