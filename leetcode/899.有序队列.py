#
# @lc app=leetcode.cn id=899 lang=python3
#
# [899] 有序队列
#

# @lc code=start
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return "".join(sorted(s))
        else:
            res = s
            m = min(s)
            for i in range(len(s)):
                if s[i] == m:
                    if s[i:]+s[:i] < res:
                        res = s[i:]+s[:i]
            return res

# @lc code=end

