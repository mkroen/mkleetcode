#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """栈实现"""
        l = []
        m = {('(', ")"), ('[', "]"), ('{', "}")}
        for each in s:
            if l and (l[-1], each) in m:
                l.pop()
            else:
                l.append(each)
        return False if l else True
# @lc code=end

S = Solution()
s = "(]"
print(S.isValid(s))
