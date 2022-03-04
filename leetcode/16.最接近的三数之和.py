#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        ans = sum(nums[:3])
        flag = abs(ans - target)
        for i in range(length):
            j = i + 1
            k = length - 1
            while True:
                if j >= k:
                    break
                if abs(nums[i] + nums[j] + nums[k] - target) < flag:
                    flag =  abs(nums[i] + nums[j] + nums[k] - target)
                    ans = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    break
        return ans
                 
# @lc code=end

S = Solution()
nums = [-100,-98,-2,-1]
target = -101
print(S.threeSumClosest(nums, target))