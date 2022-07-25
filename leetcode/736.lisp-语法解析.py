#
# @lc app=leetcode.cn id=736 lang=python3
#
# [736] Lisp 语法解析
#
from typing import List, Dict
from collections import defaultdict
# @lc code=start


class Solution:
    def evaluate(self, expression: str) -> int:
        # TODO
        pass


class Solution_v2:
    # 变量作用域没搞清楚,以为是从外向内覆盖
    # 57 / 66 WA
    def sep(self, exp: str) -> List[str]:
        if exp.startswith("(") and exp.endswith(")"):
            exp = exp[1:-1]
        res = []
        start = 0
        dep = 0
        for i in range(len(exp)):
            if exp[i] == "(":
                if dep == 0:
                    start = i
                dep += 1
            elif exp[i] == ")":
                dep -= 1
                if dep == 0:
                    res.append(exp[start:i+1])
                    start = i+2
            elif dep:
                continue
            elif exp[i] == " ":
                if i > start:
                    res.append(exp[start:i])
                    start = i+1
        if exp[start:]:
            res.append(exp[start:])
        return res

    def get_value(self, exp: str, v: Dict = {}) -> int:
        l = self.sep(exp)
        if len(l) == 1:
            self.get_value(
                l[-1], v) if l[-1].startswith("(") else v.get(l[-1]) or int(l[-1])
        elif l[0] == "let":
            i = 1
            max_index = len(l)-1
            while i+1 < max_index:
                v[l[i]] = self.get_value(
                    l[i+1], v) if l[i+1].startswith("(") else v.get(l[i+1]) or int(l[i+1])
                i += 2
            return self.get_value(l[-1], v) if l[-1].startswith("(") else v.get(l[-1]) or int(l[-1])
        elif l[0] == "add" or l[0] == "mult":
            n1 = v.get(l[1])
            n2 = v.get(l[2])
            if n1 == None:
                n1 = self.get_value(l[1], v) if l[1].startswith(
                    "(") else v.get(l[1], int(l[1]))
            if n2 == None:
                n2 = self.get_value(l[2], v) if l[2].startswith(
                    "(") else v.get(l[2], int(l[2]))
            return n1+n2 if l[0] == "add" else n1*n2
        else:
            return 0

    def evaluate(self, expression: str) -> int:
        return self.get_value(expression)


# @lc code=end
S = Solution()
expression = "(let x0 4 x1 -2 x2 3 x3 -5 x4 -3 x5 -1 x6 3 x7 -2 x8 4 x9 -5 (mult x2 (mult (let x0 -3 x4 -2 x8 4 (mult (let x0 -2 x6 4 (add x5 x2)) x3)) (mult (mult -7 (mult -9 (let x0 -2 x7 3 (add -10 x0)))) x6))))"

# print(S.sep(expression))
print(S.evaluate(expression))
