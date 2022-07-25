#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#
from typing import List
# @lc code=start
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel]+[0]*len(stations)
        for i, (dis, fuel) in enumerate(stations):
            for j in range(i, -1 ,-1):
                if dp[j] >= dis:
                    dp[j+1] = max(dp[j+1], dp[j]+fuel)
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        else:
            return -1
# @lc code=end

