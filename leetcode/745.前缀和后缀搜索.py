#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#
from typing import List
# @lc code=start


class WordFilter:
    # 暴力存字典过。。

    def __init__(self, words: List[str]):
        self.d = {}
        for index, w in enumerate(words):
            for i in range(1, len(w)+1):
                for j in range(len(w)):
                    self.d[(w[:i], w[j:])] = index

    def f(self, pref: str, suff: str) -> int:
        return self.d.get((pref, suff), -1)


class WordFilter_v2:
    # 暴力比对
    # 超时 13 / 17 个通过测试用例

    def __init__(self, words: List[str]):
        self.l = words
        self.s = {}

    def f(self, pref: str, suff: str) -> int:
        if self.s.get((pref, suff)):
            return self.s[(pref, suff)]
        res = -1
        for index, w in enumerate(self.l):
            if w.startswith(pref) and w.endswith(suff):
                res = index
        self.s[(pref, suff)] = res
        return res

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end
