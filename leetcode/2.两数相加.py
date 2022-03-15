#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        chain = ans
        overflow = False
        while(l1 or l2):
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            num = num1 + num2 + overflow
            overflow = True if num >= 10 else False
            chain.next = ListNode(num % 10)
            chain = chain.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if overflow:
            chain.next = ListNode(1)
        return ans.next
# @lc code=end

