#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#
from typing import List
# @lc code=start


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        n = len(logs)
        for l in logs:
            a, b, c = l.split(":")
            a = int(a)
            c = int(c)
            if b == "start":
                stack.append([a, c])
            else:
                last = stack.pop()
                res[a] += c-last[1]+1
                for i in range(len(stack)):
                    stack[i][1] += c-last[1]+1
        return res
# @lc code=end
