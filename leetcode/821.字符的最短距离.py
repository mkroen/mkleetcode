#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
from typing import List
# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        st = False
        si = 0
        for i in range(len(s)):
            if s[i] == c:
                st = True
                si = 1
                ans.append(0)
                f = 1
                i -= 1
                while i >= 0:
                    if ans[i] > f:
                        ans[i] = f
                        i -= 1
                        f += 1
                    else:
                        break
            elif st:
                ans.append(si)
                si += 1
            else:
                ans.append(10001)
        return ans
# @lc code=end

S = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaab"
c = "b"
print(S.shortestToChar(s,c))