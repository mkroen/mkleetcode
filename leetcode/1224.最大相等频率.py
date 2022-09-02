#
# @lc app=leetcode.cn id=1224 lang=python3
#
# [1224] 最大相等频率
#
from typing import List
# @lc code=start


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        c = {}
        cc = {}
        res = 1
        for i, n in enumerate(nums):
            if c.get(n):
                if cc[c[n]] == 1:
                    cc.pop(c[n])
                else:
                    cc[c[n]] -= 1
                c[n] += 1
                cc[c[n]] = cc.get(c[n], 0) + 1
            else:
                c[n] = 1
                cc[1] = cc.get(1, 0) + 1
            if len(cc) == 1 and (list(cc.values())[0] == 1 or list(cc.keys())[0] == 1):
                res = i+1
            elif len(cc) == 2:
                k = list(cc.keys())
                if cc[max(k)] == 1 and max(k) - min(k) == 1 or min(k) == 1 and cc[min(k)] == 1:
                    res = i+1
        return res


# @lc code=end
S = Solution()
# n = [i//2 for i in range(10**6)]
# print(S.maxEqualFreq(nums=n))
print(S.maxEqualFreq(nums=[1, 2]))
