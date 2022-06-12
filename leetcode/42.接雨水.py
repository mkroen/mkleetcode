#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import List
# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_h = 0
        max_index = -1
        for i, h in enumerate(height):
            if i != 0 and height[i] > height[i-1]:
                low = 0
                high = min(max_h, h)
                index = i
                while True:
                    if index == 0 or index == max_index:
                        break
                    index -= 1
                    low = max(height[index], low)
                    diff = high - low
                    if diff <= 0:
                        break
                    # print(f"add {index} {high-low}")
                    res += high - low
                    low = max(low, height[index])
            if height[i] >= max(max_h, height[i]):
                max_h = height[i]
                max_index = i
        return res

# @lc code=end


S = Solution()
height = [4, 2, 0, 3, 2, 5]
print(S.trap(height))
