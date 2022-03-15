#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char = ''
        for each in s:
            if each not in char:
                char += each
            else:
                if len(char) > max_len:
                    max_len = len(char)
                index = char.index(each)
                char += each
                char = char[index+1:]
        if len(char) > max_len:
            max_len = len(char)
        return max_len

# @lc code=end

