#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """AC"""
        ans = s[0]
        ans_len = 1
        global max_len,length
        max_len = len(s)
        def fun(start,end):
            global length
            if start-1>=0 and end+1<max_len:
                if s[start-1] == s[end+1]:
                    length += 2
                    return fun(start-1,end+1) or s[start:end+1]
            return s[start:end+1]
        for i in range(max_len):
            length = 1
            string = fun(i,i)
            if length > ans_len:
                ans_len = length
                ans = string
            if i+1 < max_len and s[i] == s[i+1]:
                length = 2
                string = fun(i,i+1)
                if length > ans_len:
                    ans_len = length
                    ans = string
        return ans
    
    def longestPalindrome_v2(self, s: str) -> str:
        """TLE"""
        max_len = len(s)
        ans = s[0]
        ans_len = 1
        # import pdb
        # pdb.set_trace()
        for i in range(max_len):
            for j in range(i+1, max_len):
                if 2*j-2*i <= ans_len:
                    continue
                head = s[i:j]
                if head + head[::-1] == s[i:2*j-i]:
                    if ans_len < 2*j-2*i:
                        ans_len = 2*j-2*i
                        ans = s[i:2*j-i]
                elif head + head[::-1][1:] == s[i:2*j-i-1]:
                    if ans_len < 2*j-2*i-1:
                        ans_len = 2*j-2*i-1
                        ans = s[i:2*j-i-1]
                if ans_len >= max_len-i:
                    break
            
        return ans
# @lc code=end

S = Solution()
s = "abbccbbcbbdddddddd"
import datetime
a = datetime.datetime.now()
print(S.longestPalindrome(s))
b = datetime.datetime.now()
print(b-a)