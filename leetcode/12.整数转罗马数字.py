#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        length = len(str(num))
        roma = [("M", "", ""), ("C", "D", "M"), ("X", "L", "C"), ("I", "V", "X")]
        roma = roma[-length:]
        ans = ""
        for i in range(length):
            if length - i - 1 == 0:
                number = num
            else:
                number = num // 10**(length-i-1)
            a, b, c = roma[i]
            if number == 0:
                continue
            elif number <= 3:
                ans += a*number
            elif number == 4:
                ans += a + b
            elif number <= 8:
                ans += b + a*(number-5)
            else:
                ans += a + c
            num = num % 10**(length-i-1)
        return ans


# @lc code=end
S = Solution()
num = 1994
print(S.intToRoman(num))
