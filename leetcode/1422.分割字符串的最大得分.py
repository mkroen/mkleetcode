#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        score = s[1:].count("1") + (s[0] == "0")
        res = score
        for each in s[1:-1]:
            if each == "0":
                score += 1
            else:
                score -= 1
            res = max(res, score)
        return res

# @lc code=end

S = Solution()
print(S.maxScore('1111'))