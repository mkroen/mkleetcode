#
# @lc app=leetcode.cn id=757 lang=python3
#
# [757] 设置交集大小至少为2
#
from typing import List
# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        rl = []
        last = None
        for each in intervals:
            if each[0] == last:
                continue
            else:
                last = each[0]
                rl.append(each)
        i = len(rl)-1
        last = (rl[i][0], rl[i][0]+1)
        while i>0:
            i-=1
            if last[0]>rl[i][1]:
                ans += 2
                last = (rl[i][0], rl[i][0]+1)
            elif last[0] <= rl[i][1] < last[1]:
                ans += 1
                last = (rl[i][0], last[0])
            elif rl[i][0]<=last[0] and last[1]<=rl[i][1]:
                continue
        return ans+2

# @lc code=end
S = Solution()
print(S.intersectionSizeTwo(intervals = [[6,21],[1,15],[15,20],[10,21],[0,7]]))
