#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
from typing import List, Optional
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        head = ListNode()
        node_sum = len(lists)
        node = head
        while True:
            num = 10001
            num_index = 0
            empty_node = 0
            for index, each in enumerate(lists):
                if each:
                    if each.val < num:
                        num = each.val
                        num_index = index
                else:
                    empty_node += 1
            if empty_node == node_sum:
                break
            next_node = lists[num_index]
            node.next = next_node
            node = node.next
            lists[num_index] = next_node.next
            if not next_node.next:
                empty_node += 1
                if empty_node == node_sum:
                    break
        return head.next
                

# @lc code=end
S = Solution()
a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))
# lists = [a, b, c]
lists = [None]
S.mergeKLists(lists)