#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
from types import resolve_bases


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """使用栈
        ["(",2,"("]  next:")"
        => ["(", 2, 2] => ["(", 4]
        计算深度，如果有深度,出栈并将相邻数字合并
        """
        res = 0
        l = []
        dep = 0
        for each in s:
            if each == "(":
                l.append(each)
                dep += 1
            else:
                if dep:
                    dep -= 1
                    n = 2
                    while True:
                        a = l.pop()
                        if not isinstance(a, str):
                            n += a
                        else:
                            break
                    while True:
                        if not l:
                            break
                        if not isinstance(l[-1], str):
                            n += l.pop()
                        else:
                            break
                    l.append(n)
                    if n > res:
                        res = n
                else:
                    l.append(each)
        return res


# @lc code=end
S = Solution()
s = "(()(()(()(()(()(()(()"
print(S.longestValidParentheses(s))
