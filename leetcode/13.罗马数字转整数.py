#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roma = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        last = None
        for each in s[::-1]:
            if last and roma[each] < roma[last]:
                ans -= roma[each]
            else:
                ans += roma[each]
            last = each
        return ans
            

# @lc code=end
S = Solution()
s = "MCMXCIV"
print(S.romanToInt(s))
