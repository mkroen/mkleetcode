#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.count = 0
        l = [root]
        while l:
            n = l.pop()
            self.count += 1
            if n.left:
                l.append(n.left)
            if n.right:
                l.append(n.right)

    def insert(self, val: int) -> int:
        r = self.root
        self.count += 1
        index = bin(self.count)[3:]
        for each in index[:-1]:
            if each == "0":
                r = r.left
            else:
                r = r.right
        if index[-1] == "0":
            r.left = TreeNode(val)
        else:
            r.right = TreeNode(val)
        return r.val

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# @lc code=end
