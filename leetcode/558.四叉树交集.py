#
# @lc app=leetcode.cn id=558 lang=python3
#
# [558] 四叉树交集
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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # 卡着过的 应该用二分
        def get_dep(tree: 'Node', dep=0):
            if tree.isLeaf:
                return dep
            else:
                return dep+max(get_dep(tree.topLeft, dep+1),
                               get_dep(tree.topRight, dep+1),
                               get_dep(tree.bottomLeft, dep+1),
                               get_dep(tree.bottomRight, dep+1))
        depth = max(get_dep(quadTree1), get_dep(quadTree2))
        n = 2**depth
        t1 = [[0]*n for _ in range(n)]
        t2 = [[0]*n for _ in range(n)]

        def treeset(t: List[List[int]], tree: 'Node', x1, y1, x2, y2):
            if tree.isLeaf and tree.val:
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        t[x][y] = 1
            elif not tree.isLeaf:
                treeset(t, tree.topLeft, x1, y1, (x1+x2-1)//2, (y1+y2-1)//2)
                treeset(t, tree.topRight, x1, (y1+y2+1)//2, (x1+x2-1)//2, y2)
                treeset(t, tree.bottomLeft, (x1+x2+1)//2, y1, x2, (y1+y2-1)//2)
                treeset(t, tree.bottomRight, (x1+x2+1) //
                        2, (y1+y2+1)//2, x2, y2)
        treeset(t1, quadTree1, 0, 0, n-1, n-1)
        treeset(t2, quadTree2, 0, 0, n-1, n-1)
        for i in range(n):
            for j in range(n):
                t1[i][j] = t1[i][j] or t2[i][j]

        def fun(x1, y1, x2, y2):
            if x1 == x2:
                return Node(t1[x1][y1], 1, None, None, None, None)
            else:
                flag = t1[x1][y1]
                for i in range(x1, x2+1):
                    for j in range(y1, y2+1):
                        if t1[i][j] != flag:
                            return Node(flag, 0, fun(x1, y1, (x1+x2-1)//2, (y1+y2-1)//2), fun(x1, (y1+y2+1)//2, (x1+x2-1)//2, y2), fun((x1+x2+1)//2, y1, x2, (y1+y2-1)//2), fun((x1+x2+1)//2, (y1+y2+1)//2, x2, y2))
                return Node(flag, 1, None, None, None, None)
        res = fun(0, 0, n-1, n-1)
        return res

# @lc code=end
