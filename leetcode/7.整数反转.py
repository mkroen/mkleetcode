#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """AC"""
        if not x:
            return x
        MIN = -2147483648
        MAX = 2147483647
        negative = False
        if x<0:
            negative = True
            s = str(-x)
        else:
            s = str(x)
        s = s[::-1]
        zero = 0
        for index, each in enumerate(s):
            if each == "0":
                zero += 1
            else:
                break
        s = int(s[zero:])
        if negative:
            s = -s
        if s<MIN or s>MAX:
            return 0
        return s
        

# @lc code=end

x = -2147483648
S = Solution()
print(S.reverse(x))