#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """正常遍历"""
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False
# @lc code=end

