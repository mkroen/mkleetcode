#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """根据三数之和的逻辑改动来，在外层多加了一层循环"""
        res = []
        length = len(nums)
        if length < 4:
            return res
        nums.sort()
        for n in range(length):
            if nums[n] > target//4+1:
                break
            if n > 0 and nums[n] == nums[n-1]:
                continue
            for i in range(n+1, length):
                j = i+1
                k = length-1
                if i != n+1 and nums[i] == nums[i-1]:
                    continue
                while True:
                    if j >= k:
                        break
                    if nums[n] + nums[i] + nums[j] + nums[k] == target:
                        res.append([nums[n], nums[i], nums[j], nums[k]])
                        k -= 1
                        j += 1
                        while True:
                            if j >= k:
                                break
                            if nums[j] == nums[j-1]:
                                j += 1
                            else:
                                break
                    elif nums[n] + nums[i] + nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        j += 1        
        return res
# @lc code=end

S = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(S.fourSum(nums, target))