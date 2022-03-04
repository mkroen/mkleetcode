#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        node = head
        new_head = None
        last_node = None
        while True:
            if not node or not node.next:
                break
            next_node = node.next
            node.next = next_node.next
            next_node.next = node
            if last_node:
                last_node.next = next_node
            else:
                new_head = next_node
            last_node = node
            node = node.next
        return new_head or head
    
# @lc code=end

S = Solution()
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
S.swapPairs(a)