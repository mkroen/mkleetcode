#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
from typing import List
# @lc code=start


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        if all(c.isdigit() for c in expression):
            return [int(expression)]
        for i, c in enumerate(expression):
            if not c.isdigit():
                ans += [eval(f'{a}{c}{b}')
                        for a in self.diffWaysToCompute(expression[:i])
                        for b in self.diffWaysToCompute(expression[i+1:])]
        return ans

    def get_value(self, n: int, m: int, s: str) -> int:
        if s == "*":
            return n*m
        elif s == "-":
            return n-m
        elif s == "+":
            return n+m
        else:
            return 0

    def diffWaysToCompute_v2(self, expression: str) -> List[int]:
        # 思路是ok的，但测试用例没去重
        import sys
        sys.setrecursionlimit(1000000)
        res = []
        calc = {"+", "-", "*"}

        def cal(lst: List):
            if len(lst) == 1:
                nonlocal res
                res.append(lst[0])
                return
            nonlocal calc
            l = len(lst)
            for i in range(l):
                if lst[i] in calc:
                    cal(lst[:i-1] + [self.get_value(lst[i-1],
                        lst[i+1], lst[i])]+lst[i+2:])

        l = []
        i = ""
        for e in expression:
            if e in "*+-":
                l.append(int(i))
                l.append(e)
                i = ""
            else:
                i += e
        l.append(int(i))
        cal(l)
        return res


class Solution2:
    # 审题问题。以为是+*-的运算顺序
    def get_value(self, n: int, m: int, s: str) -> int:
        if s == "*":
            return n*m
        elif s == "-":
            return n-m
        elif s == "+":
            return n+m
        else:
            return 0

    def cal(self, lst: List[str], s: str) -> List[str]:
        l = len(lst)
        i = 0
        while i != l:
            if lst[i] == s:
                lst = lst[:i-1] + \
                    [self.get_value(lst[i-1], lst[i+1], s)]+lst[i+2:]
                l -= 2
            else:
                i += 1
        return lst

    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        l = []
        i = ""
        for e in expression:
            if e in "*+-":
                l.append(int(i))
                l.append(e)
                i = ""
            else:
                i += e
        l.append(int(i))
        cals = ["*-+", "*+-", "+*-", "+-*", "-+*", "-*+"]
        for c in cals:
            ll = l.copy()
            for each in c:
                ll = self.cal(ll, each)
        if ll[0] not in res:
            res.append(ll[0])
        return res


# @lc code=end


S = Solution()
print(S.diffWaysToCompute(expression="2-1-1"))
# print(S.cal([2, "-", 1, "-", 1], "-"))
