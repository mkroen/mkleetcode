#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """py yyds"""
        try:
            return haystack.index(needle)
        except:
            return -1
# @lc code=end

