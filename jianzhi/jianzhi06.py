# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        if not head:
            return res
        while head.next != None:
            res.append(head.val)
            head = head.next
        res.append(head.val)
        return res[::-1]


# 执行用时：40 ms, 在所有 Python3 提交中击败了54.32%的用户
# 内存消耗：16.2 MB, 在所有 Python3 提交中击败了96.23%的用户
# 通过测试用例：24 / 24