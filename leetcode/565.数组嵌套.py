#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#
from typing import List
# @lc code=start


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        res = set()
        for n in nums:
            if n in res:
                continue
            turn = [n]
            t_set = {n}
            while True:
                n = nums[n]
                if n in t_set:
                    index = turn.index(n)
                    res = res.union(set(turn[index:]))
                    ans = max(ans, len(turn[index:]))
                    break
                elif n in res:
                    break
                else:
                    turn.append(n)
                    t_set.add(n)
        return ans
# @lc code=end
