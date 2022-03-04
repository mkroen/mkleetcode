#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """取自大佬的解决方法
        由于0 <= nums.length <= 3000
        可考虑排序解决
        """
        res = []
        length = len(nums)
        if length < 3:
            return res
        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = length-1
            while True:
                if j >= k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while True:
                        if j >= k:
                            break
                        if nums[j] == nums[j-1]:
                            j += 1
                        else:
                            break
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1        
        return res

    def threeSum_v2(self, nums: List[int]) -> List[List[int]]:
        """AC，使用map达到O1的取速度，复杂度为On**2，但看起来还是有点慢"""
        num_map = {}
        ans = set()
        for each in nums:
            num_map[each] = num_map.get(each, 0) + 1
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if index_i == index_j:
                    continue
                k = -i-j
                sum_k = 1 + (k==i) + (k==j)
                if num_map.get(k, -1) >= sum_k:
                    tp = [i, j, k]
                    tp.sort()
                    ans.add(tuple(tp))
        return [list(each) for each in ans]
# @lc code=end

S = Solution()
nums = [-1,0,1,2,-1,-4]
print(S.threeSum(nums))