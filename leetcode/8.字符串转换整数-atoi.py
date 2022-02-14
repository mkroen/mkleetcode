#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        """AC,sb题"""
        if not s:
            return 0
        MIN = -2147483648
        MAX = 2147483647
        negative = False
        first_index = 0
        x = []
        first = True
        for each in s:
            if first:
                if each == " ":
                    continue
                if each.isdigit() or each in ("+", "-"):
                    first = False
                    x.append(each)
                else:
                    return 0
            elif each.isdigit():
                x.append(each)
            else:
                break
        if not x:
            return 0
        if x[0] in ("+", "-"):
            if x[0] == "-":
                negative = True
            x = x[1:]
        for each in x:
            if each == "0":
                first_index += 1
            else:
                break
        x = x[first_index:]
        if not x:
            return 0
        ans = int("".join(x)) * (-1 if negative else 1)
        if ans < MIN:
            ans = MIN
        elif ans > MAX:
            ans = MAX
        return ans 

    def myAtoi_v2(self, s: str) -> int:
        import re
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31) # type: ignore

# @lc code=end


S = Solution()
s = "   123"
print(S.myAtoi(s))
print(S.myAtoi_v2(s))