#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = "".join(sorted(s))
            if res.get(key):
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())

# @lc code=end
