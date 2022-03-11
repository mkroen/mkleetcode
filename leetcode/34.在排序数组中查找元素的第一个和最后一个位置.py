#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分查找 然后左右扩散
        """
        res = [-1, -1]
        if not nums:
            return res
        start = 0
        index = None
        length = len(nums)
        if length == 1:
            if target == nums[0]:
                return [0, 0]
            else:
                return res
        end = length - 1
        while start <= end:
            mid = (start+end)//2
            if target == nums[mid]:
                index = mid
                break
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if index is not None:
            start = index
            end = index
            while True:
                if start < 0:
                    start = 0
                    break
                if nums[start] == target:
                    start -= 1
                else:
                    start += 1
                    break
            while True:
                if end > length-1:
                    end = length-1
                    break
                if nums[end] == target:
                    end += 1
                else:
                    end -= 1
                    break
            res = [start, end]
        return res
# @lc code=end
S = Solution()
nums = [10, 10]
target = 10
print(S.searchRange(nums, target))
