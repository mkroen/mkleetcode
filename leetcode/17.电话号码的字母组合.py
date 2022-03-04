#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [""]
        if not digits:
            return []
        digits_map = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }
        for d in digits:
            new_res = []
            for r in res:
                for m in digits_map[d]:
                    new_res.append("".join((r, m)))
            res = new_res.copy()
        return res
# @lc code=end

S = Solution()
digits = "2"
print(S.letterCombinations(digits))