#
# @lc app=leetcode.cn id=998 lang=python3
#
# [998] 最大二叉树 II
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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
        last = None
        node = root
        while node:
            if node.val < val:
                n = TreeNode(val=val, left=node)
                if last:
                    last.right = n
                return root if last else n
            else:
                last = node
                node = node.right
        last.right = TreeNode(val=val)
        return root


# @lc code=end
