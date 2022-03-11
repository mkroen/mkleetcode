#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        # nums = [6, 5, 8, 10, 9, 7, 4, 3, 2, 1]
        # [6, 5, 9, 1, 2, 3, 4, 7, 8, 10]
        # 找到最靠右的 右边有更大的 8,9
        # 9 放到 8
        # 倒排 7, 4, 3, 2, 1
        # 正排 8, 10
        """
        length = len(nums)
        left = 0
        right = 0
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] < nums[j]:
                    left, right = i, j
        if left != right:
            num = nums[right]
            extra_nums = nums[left:right]
            extra_nums.sort()
            nums[left] = num
            start_index = left+1
            for each in nums[right+1:][::-1]:
                nums[start_index] = each
                start_index += 1
            for each in extra_nums:
                nums[start_index] = each
                start_index += 1
        else:
            nums.sort()
        return
# @lc code=end
global nums
# nums = [4,2,0,2,3,2,0]
# nums = [1, 2, 2, 2, 2, 2]
nums = [6, 5, 8, 9, 7, 4, 3, 2, 1]
# [6, 5, 9, 1, 2, 3, 4, 7, 8]
S = Solution()
S.nextPermutation(nums)
print(nums)