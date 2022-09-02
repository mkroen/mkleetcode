#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#
# wa两发
# <=2 wa
# map(abs, res) wa

import re
# @lc code=start


def gcd(a, b) -> int:
    if a < b:
        a, b = b, a
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b


def lcm(a, b) -> int:
    return a*b//gcd(a, b)


class Solution:
    def fractionAddition(self, expression: str) -> str:
        exp = re.findall("[-+]?[0-9]+/[0-9]+", expression)
        l = []
        for e in exp:
            if e[0] == "-":
                flag = -1
                e = e[1:]
            elif e[0] == "+":
                flag = 1
                e = e[1:]
            else:
                flag = 1
            n, d = map(int, e.split("/"))
            l.append((flag*n, d))
        res = [0, 1]
        for n, d in l:
            if res[0] == 0:
                res[0] = n
                res[1] = d
                continue
            lcm_num = lcm(res[1], d)
            res[0] = res[0]*(lcm_num//res[1])+n*(lcm_num//d)
            res[1] = lcm_num
        if res[0] == 0:
            res[1] = 1
        else:
            i = 2
            while i <= min(map(abs, res)):
                if res[0] % i == 0 and res[1] % i == 0:
                    res[0] = res[0] // i
                    res[1] = res[1] // i
                else:
                    i += 1
        return f"{res[0]}/{res[1]}"


# @lc code=end

S = Solution()
print(S.fractionAddition(expression="-1/4-4/5-1/4"))
