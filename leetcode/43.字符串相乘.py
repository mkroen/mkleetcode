#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        l1 = len(num1)
        l2 = len(num2)
        res = [0] * (l1 + l2)
        for i in range(l1):
            for j in range(l2):
                a, b = divmod(int(num1[i])*int(num2[j]), 10)
                res[i+j] += a
                res[i+j+1] += b
        for i in range(l1+l2-1, 0, -1):
            res[i-1] += res[i]//10
            res[i] %= 10
        index = 0 if (res[0] != 0) else 1
        return "".join(str(r) for r in res[index:])


# @lc code=end
S = Solution()
print(S.multiply(num1="999", num2="999"))
