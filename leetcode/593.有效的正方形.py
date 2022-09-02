#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#
from typing import List, Set
# @lc code=start


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 另可用正方形判断法则
        # 如果两条斜边的中点相同：则说明以该两条斜边组成的四边形为「平行四边形」。
        # 在满足「条件一」的基础上，如果两条斜边的长度相同：则说明以该两条斜边组成的四边形为「矩形」。
        # 在满足「条件二」的基础上，如果两条斜边的相互垂直：则说明以该两条斜边组成的四边形为「正方形」。

        l: List[Set] = []
        for pi in [p1, p2, p3, p4]:
            p_s = set()
            for pj in [p1, p2, p3, p4]:
                if pi == pj:
                    continue
                p_s.add((pi[0]-pj[0])**2+(pi[1]-pj[1])**2)
            l.append(p_s)
        common = l[0].intersection(l[1]).intersection(l[2]).intersection(l[3])
        all_l = l[0].union(l[1]).union(l[2]).union(l[3])
        if len(all_l) > 2:
            return False
        for each in common:
            if 2*each in common:
                return True
        return False


# @lc code=end
S = Solution()
print(S.validSquare([1, 1],
                    [0, 1],
                    [1, 2],
                    [0, 0]))
