#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """深度递归"""
        def match(s: str, p: str) -> bool:
            if not p and not s:
                return True
            if not p and s:
                return False
            len_p = len(p)
            if len_p >= 2:
                ms = p[0]
                mf = p[1]
                if mf == "*":
                    if ms == ".":
                        # 匹配任意字符n次
                        for i in range(len(s)+1):
                            if match(s[i:], p[2:]):
                                return True
                        return False
                    else:
                        # 匹配0次
                        if match(s, p[2:]):
                            return True
                        for i in range(len(s)):
                            if s[i] == ms:
                                if match(s[i+1:], p[2:]):
                                    return True
                            else:
                                break
                        return False
            if len_p >= 1:
                ms = p[0]
                if ms == ".":
                    if not s:
                        return False
                    return match(s[1:], p[1:])
                else:
                    if not s:
                        return False
                    if s[0] == ms:
                        return match(s[1:], p[1:])
                    return False
            else:
                return False
        return match(s,p)
# @lc code=end

S = Solution()
# s = "mississippi"
# p = "mis*is*p*."
s = "ab"
p = ".*c"
print(S.isMatch(s,p))

