#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#
from typing import List
# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return ""
        ans = ""
        words_map = {}
        for w in words:
            if words_map.get(w[0]):
                words_map[w[0]].append(w)
            else:
                words_map[w[0]] = [w]
        for alpha in "abcdefghijklmnopqrstuvwxyz":
            if not words_map.get(alpha):
                continue
            ws = words_map[alpha]
            count_map = [[] for _ in range(30)]
            for w in ws:
                count_map[len(w)-1].append(w)
            last_map = {""}
            for i in range(30):
                this_map = count_map[i]
                if not this_map:
                    break
                this_map.sort()
                next_last_map = set()
                for j in this_map:
                    if j[0:i] in last_map:
                        if len(j) > len(ans):
                            ans = j
                        next_last_map.add(j)
                last_map = next_last_map
        return ans

# @lc code=end
S = Solution()
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(S.longestWord(words))
