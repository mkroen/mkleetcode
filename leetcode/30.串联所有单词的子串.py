#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
from typing import List
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """滑动窗口 往后一个一个对应 用map和set存 内存应该还能优化"""
        ans = []
        len_s = len(s)
        len_w = len(words[0])
        count_w = len(words)
        len_windows = count_w*len_w
        if len_s < len_windows:
            return ans
        total_word = {}
        word_set = set()
        for w in words:
            total_word[w] = (total_word.get(w) or 0) + 1
            word_set.add(w)
        start = 0
        flag = False
        need_word = total_word.copy()
        while True:
            flag = True
            if len_s - start < len_windows:
                break
            for i in range(start, start+len_windows, len_w):
                if s[i:i+len_w] in word_set and need_word[s[i:i+len_w]] >= 1:
                    need_word[s[i:i+len_w]] -= 1
                else:
                    flag = False
                    need_word = total_word.copy()
                    break
            if flag:
                ans.append(start)
            start += 1
            need_word = total_word.copy()
        return ans
                

    def findSubstring_v2(self, s: str, words: List[str]) -> List[int]:
        """题目理解偏差 以为给的全是定长单词 滑动窗口滑多了
        s = "ling mind raboo fooowingdingbarrwingmonkeypoundcake"
        words = ["fooo","barr","wing","ding","wing"]
        对于上述情况 s的单词不一定都是4个
        所以只能一个一个往后滑
        """
        ans = []
        len_s = len(s)
        len_w = len(words[0])
        count_w = len(words)
        len_windows = count_w*len_w
        if len_s < len_windows:
            return ans
        total_word = {}
        word_set = set()
        for w in words:
            total_word[w] = (total_word.get(w) or 0) + 1
            word_set.add(w)
        start = 0
        flag = False
        need_word = total_word.copy()
        while True:
            if len_s - start < len_windows:
                break
            if flag:
                the_last = s[start-len_w:start]
                the_next = s[start+len_windows-len_w:start+len_windows]
                if the_next not in word_set:
                    start += len_windows
                    need_word = total_word.copy()
                    flag = False
                    continue
                need_word[the_last] += 1
                need_word[the_next] -= 1
                success = True
                for v in need_word.values():
                    if v != 0:
                        success = False
                        break
                if success:
                    ans.append(start)
                start += len_w
            else:
                judge = True
                for i in range(start, start+len_windows, len_w):
                    if s[i: i+len_w] in word_set:
                        need_word[s[i: i+len_w]] -= 1
                    else:
                        start = i+len_w
                        need_word = total_word.copy()
                        judge = False
                        break
                if judge:
                    flag = True
                    success = True
                    for v in need_word.values():
                        if v != 0:
                            success = False
                            break
                    if success:
                        ans.append(start)
                    start += len_w
        return ans
# @lc code=end

S = Solution()
# s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words = ["fooo","barr","wing","ding","wing"]
s = "aaa"
words = ["a","a"]
print(S.findSubstring(s, words))