#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        二分查找 每次往前后多对比一位
        """
        if not nums:
            return 0
        length = len(nums)
        left, right = 0, length - 1
        while True:
            # if left > right:
            #     break
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if mid >= length - 1:
                    return length
                if target <= nums[mid+1]:
                    return mid+1
                else:
                    left = mid+2
            else:
                if mid <= 0:
                    return 0
                if target == nums[mid-1]:
                    return mid-1
                elif target > nums[mid-1]:
                    return mid
                else:
                    right = mid-1
# @lc code=end
S = Solution()
nums = [1,3,5,6]
target = 0
print(S.searchInsert(nums,target))
