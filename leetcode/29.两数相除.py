#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """思路：竖式相除"""
        flag = (dividend >= 0) ^ (divisor >= 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        s1 = str(abs(dividend))
        s2 = str(abs(divisor))
        res = []
        if flag:
            res.append("-")
        total = len(s1)
        index = len(s2)
        if index > total:
            return 0
        while True:
            a = int(s1[:index])
            ans = 0
            while True:
                if a >= divisor:
                    a -= divisor
                    ans += 1
                else:
                    break
            s1 = (str(a)+s1[index:]).rjust(total, "0")
            res.append(str(ans))
            if index == total:
                break
            index += 1
        return int("".join(res)) if -2147483648 <= int("".join(res)) <= 2147483647 else 2147483647

# @lc code=end
S = Solution()
print(S.divide(102137742,1002137743))
