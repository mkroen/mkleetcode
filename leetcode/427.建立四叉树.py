#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#
from typing import List
# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def fun(x1, y1, x2, y2):
            if x1 == x2:
                return Node(grid[x1][y1], 1, None, None, None, None)
            else:
                flag = grid[x1][y1]
                for i in range(x1, x2+1):
                    for j in range(y1, y2+1):
                        if grid[i][j] != flag:
                            return Node(flag, 0, fun(x1, y1, (x1+x2-1)//2, (y1+y2-1)//2), fun(x1, (y1+y2+1)//2, (x1+x2-1)//2, y2), fun((x1+x2+1)//2, y1, x2, (y1+y2-1)//2), fun((x1+x2+1)//2, (y1+y2+1)//2, x2, y2))
                return Node(flag, 1, None, None, None, None)
        res = fun(0, 0, len(grid)-1, len(grid)-1)
        return res

# @lc code=end
