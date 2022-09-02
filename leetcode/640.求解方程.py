#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        l = [0, 0]
        n = len(equation)
        i = 1
        flag = 1
        symbols = {"+", "-", "="}
        s = equation[0]
        while True:
            if i < n:
                while i < n and equation[i] not in symbols:
                    s += equation[i]
                    i += 1
            if s[-1] == "x":
                if len(s) == 1:
                    l[0] += flag
                elif len(s) == 2:
                    if s[0] == "+":
                        l[0] += flag
                    elif s[0] == "-":
                        l[0] -= flag
                    else:
                        l[0] += flag * int(s[0])
                else:
                    l[0] += flag * int(s[:-1])
            else:
                l[1] += flag * int(s)
            if i == n:
                break
            if equation[i] == "=":
                flag = -1
                s = equation[i+1]
                i += 2
            else:
                s = equation[i]
                i += 1
        if l[0] == 0 and l[1] != 0:
            return "No solution"
        elif l[0] == 0 and l[1] == 0:
            return "Infinite solutions"
        else:
            return f"x={-l[1]//l[0]}"


# @lc code=end
