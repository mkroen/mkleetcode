#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        CF = 0
        ans = []
        while i >= 0 or j >= 0 or CF != 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            CF, a = divmod(n1+n2+CF, 10)
            ans.append(str(a))
            i -= 1
            j -= 1
        return "".join(ans[::-1])


# @lc code=end
S = Solution()
print(S.addStrings(num1 = "0", num2 = "0"))
