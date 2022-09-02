#
# @lc app=leetcode.cn id=761 lang=python3
#
# [761] 特殊的二进制序列
#

# @lc code=start
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return s
        l = []
        c = 0
        start = 0
        for i, e in enumerate(s):
            if e == "1":
                c += 1
            else:
                c -= 1
            if c == 0:
                l.append(s[start:i+1])
                start = i+1
        if len(l) == 1:
            return "1" + self.makeLargestSpecial(l[0][1:-1]) + "0"
        for i in range(len(l)):
            if len(l[i]) > 2:
                l[i] = self.makeLargestSpecial(l[i])
        l.sort(reverse=True)
        return "".join(l)
# @lc code=end
