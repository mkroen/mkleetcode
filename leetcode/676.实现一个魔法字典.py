#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#
from typing import List
# @lc code=start


class MagicDictionary:

    def __init__(self):
        self.l = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.l = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.l:
            if len(word) != len(searchWord):
                continue
            use = True
            flag = True
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    if use:
                        use = False
                    else:
                        flag = False
                        break
            if flag and not use:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

M = MagicDictionary()
M.buildDict(["hello", "leetcode"])
print(M.search("hhllo"))