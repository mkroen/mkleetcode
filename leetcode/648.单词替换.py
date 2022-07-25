#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#
from typing import List

# @lc code=start


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d_map = {chr(i): [] for i in range(97, 123)}
        for each in dictionary:
            d_map[each[0]].append(each)
        for each in d_map.values():
            each.sort()
        l = list(sentence.split())
        for i in range(len(l)):
            for d in d_map.get(l[i][0], []):
                if len(d) > len(l[i]):
                    break
                elif l[i].startswith(d):
                    l[i] = d
                    break
        return " ".join(l)

# @lc code=end
