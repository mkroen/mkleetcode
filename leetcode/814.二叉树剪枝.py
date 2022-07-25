#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]):
            if root.left:
                if not dfs(root.left):
                    root.left = None
            if root.right:
                if not dfs(root.right):
                    root.right = None
            if not root.left and not root.right and not root.val:
                return False
            else:
                return True
        dfs(root)
        if not root.left and not root.right and not root.val:
            # [0,null,0,0,0] WA一发
            return None
        return root


# @lc code=end
