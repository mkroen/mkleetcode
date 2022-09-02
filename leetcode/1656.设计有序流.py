#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#
from typing import List
# @lc code=start


class OrderedStream:

    def __init__(self, n: int):
        self.l = [""] * n
        self.index = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        if self.index == idKey - 1:
            end = self.index + 1
            while end != len(self.l) and self.l[end]:
                end += 1
            res = self.l[self.index: end]
            self.index = end
            return res
        else:
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end
