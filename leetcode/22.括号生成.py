#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """递归深搜"""
        global ans
        ans = []
        def solve(s: str, dep: int, n: int):
            if not n and not dep:
                ans.append(s)
                return
            if dep and n:
                solve(s+"(", dep+1, n-1)
                solve(s+")", dep-1, n)
            elif not dep:
                solve(s+"(", dep+1, n-1)
            elif not n:
                solve(s+")", dep-1, n)
        solve("", 0, n)
        return ans

# @lc code=end
S = Solution()
n = 8
print(S.generateParenthesis(n))
