#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Optional
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        head = ListNode()
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
        if not list1:
            node.next = list2
        if not list2:
            node.next = list1
        return head.next
# @lc code=end

