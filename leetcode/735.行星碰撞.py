#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#
from typing import List
# @lc code=start


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            exist = True
            while res:
                if res[-1] > 0 and a < 0:
                    if abs(res[-1]) < abs(a):
                        res.pop()
                    elif abs(res[-1]) > abs(a):
                        exist = False
                        break
                    else:
                        res.pop()
                        exist = False
                        break
                else:
                    break
            if exist:
                res.append(a)
        return res


# @lc code=end
S = Solution()
print(S.asteroidCollision(asteroids=[-2,-1,1,2]))
