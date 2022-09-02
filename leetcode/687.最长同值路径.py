#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0

        def dfs(root: TreeNode, num: int) -> int:
            nonlocal res
            ans = [0]
            if root.left:
                ans.append(dfs(root.left, root.val))
            if root.right:
                ans.append(dfs(root.right, root.val))
            res = max(res, 1+sum(ans))
            if root.val == num:
                return max(ans)+1
            else:
                res = max(res, max(ans))
                return 0
        dfs(root, -1)
        return res-1


# @lc code=end
