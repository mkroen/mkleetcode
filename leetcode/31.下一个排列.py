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
        # TODO
        length = len(nums)
        index = length - 1
        while True:
            if index == 0:
                break
            num = nums[index]
            for i in range(index-1, -1, -1):
                if nums[i] < num:
                    t = index-1
                    dis = length-i
                    while True:
                        if t < i:
                            break
                        nums[t+dis-1] = nums[t]
                        t-=1
                    for j in range(i, length):
                        nums[j-1] = nums[j]
                    nums[length-1] = nums[i]
                    return
            index -= 1
        nums.sort()
        return
# @lc code=end
global nums
nums = [5, 4, 2, 3, 1]
# [5, 4, 3, 1, 2]
S = Solution()
S.nextPermutation(nums)
print(nums)