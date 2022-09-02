#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def f(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            index = 0
            num = -1
            for i in range(start, end+1):
                if nums[i] > num:
                    index = i
                    num = nums[i]
            return TreeNode(nums[index], f(start, index-1), f(index+1, end))
        return f(0, len(nums)-1)


# @lc code=end
