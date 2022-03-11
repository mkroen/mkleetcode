#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from sys import flags
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """二分,递归,Ologn"""
        length = len(nums)
        def find(left, right):
            if left > right:
                return -1
            flag = False
            if nums[right] > nums[left]:
                flag = True
                if target > nums[right] or target < nums[left]:
                    return -1
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if flag:
                    ans = find(mid+1, right)
                else:
                    ans = find(left, mid-1)
                    if ans == -1:
                        ans = find(mid+1, right)
                return ans
            else:
                if flag:
                    ans = find(left, mid-1)
                else:
                    ans = find(left, mid-1)
                    if ans == -1:
                        ans = find(mid+1, right)
                return ans
        if length == 1:
            return 0 if target == nums[0] else -1
        return find(0, length-1)
# @lc code=end
S = Solution()
nums = [1,2,3,4,5]
target = 8
print(S.search(nums, target))