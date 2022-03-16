#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        while n-1:
            n -= 1
            s_list = []
            count = 1
            last_s = s[0]
            for i in s[1:]:
                if i == last_s:
                    count += 1
                else:
                    s_list.append(f"{count}{last_s}")
                    last_s = i
                    count = 1
            s_list.append(f"{count}{last_s}")
            s = "".join(s_list)
        return s

# @lc code=end
S = Solution()
n = 30
print(S.countAndSay(n))
