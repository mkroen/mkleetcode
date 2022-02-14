# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        res = None
        while head:
            new = ListNode(head.val)
            new.next = res # type: ignore
            res = new
            head = head.next # type: ignore
        return res # type: ignore

# 执行用时：36 ms, 在所有 Python3 提交中击败了59.71%的用户
# 内存消耗：16.2 MB, 在所有 Python3 提交中击败了21.10%的用户
# 通过测试用例：27 / 27