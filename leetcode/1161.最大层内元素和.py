#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")
        num = 0
        l = [root]
        i = 0
        while l:
            i += 1
            next_l = []
            count = 0
            for each in l:
                count += each.val
                if each.left:
                    next_l.append(each.left)
                if each.right:
                    next_l.append(each.right)
            l = next_l
            if count > res:
                res = count
                num = i
        return num

# @lc code=end

