#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l = {}

        def bfs(root: Optional[TreeNode], count: int, deep: int):
            if not l.get(deep):
                l[deep] = [count, count]
            else:
                l[deep][1] = count
            if root.left:
                bfs(root.left, 2*count-1, deep+1)
            if root.right:
                bfs(root.right, 2*count, deep+1)
        bfs(root, 1, 1)
        res = max(list(l.values()), key=lambda x: x[1]-x[0])
        return res[1]-res[0]


# @lc code=end
