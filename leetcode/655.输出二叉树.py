#
# @lc app=leetcode.cn id=655 lang=python3
#
# [655] 输出二叉树
#
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def bfs(root: Optional[TreeNode]):
            if not root:
                return 0
            dep = 0
            node_list = [root]
            while node_list:
                next_list = []
                dep += 1
                for n in node_list:
                    if n.left:
                        next_list.append(n.left)
                    if n.right:
                        next_list.append(n.right)
                node_list = next_list
            return dep
        dep = bfs(root)
        res = [[""] * (2**dep-1) for _ in range(dep)]

        def dfs(root: Optional[TreeNode], start=0, end=2**dep-2, d=0):
            mid = (start+end)//2
            res[d][mid] = str(root.val)
            if root.left:
                dfs(root.left, start, mid-1, d+1)
            if root.right:
                dfs(root.right, mid+1, end, d+1)
        dfs(root)
        return res

# @lc code=end


S = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15,TreeNode(6),TreeNode(20))
print(S.printTree(root))
