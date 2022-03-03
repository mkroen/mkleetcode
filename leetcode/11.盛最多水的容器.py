#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        right_index = length - 1
        left_index = 0
        max_area = min(height[left_index], height[right_index]) * (right_index - left_index)
        while left_index < right_index:
            if height[left_index] < height[right_index]:
                max_area = max(max_area, height[left_index] * (right_index - left_index))
                left_index += 1
            else:
                max_area = max(max_area, height[right_index] * (right_index - left_index))
                right_index -= 1
        return max_area

    def maxArea_v2(self, height: List[int]) -> int:
        """对于金字塔型的情况最坏 53/60 TLE"""
        length = len(height)
        right_index = length-1
        right_num = height[right_index]
        max_right = right_num
        first = True
        max_area = min(height[0], right_num) * right_index
        while True:
            if right_index == 1:
                break
            right_num = height[right_index]
            if right_num < max_right or (right_num == max_right and not first):
                right_index -= 1
                continue
            else:
                max_right = right_num
            for left_index, left_num in enumerate(height[:right_index]):
                area = min(left_num, right_num) * (right_index - left_index)
                if area > max_area:
                    max_area = area
            right_index -= 1
        return max_area

# @lc code=end

S = Solution()
a = [1,8,6,2,5,4,8,3,7]
print(S.maxArea(a))