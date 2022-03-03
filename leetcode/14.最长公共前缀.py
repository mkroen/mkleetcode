#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        turn = 0
        while True:
            is_break = False
            alpha = ""
            for each in strs:
                try:
                    a = each[turn]
                except:
                    is_break = True
                    break
                if not alpha:
                    alpha = a
                elif alpha != a:
                    is_break = True
                    break
            turn += 1
            if is_break:
                break
            ans += alpha
        return ans

# @lc code=end
S = Solution()
a = ["dog","racecar","car"]
print(S.longestCommonPrefix(a))