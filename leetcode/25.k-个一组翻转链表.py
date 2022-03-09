#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """常数空间，节点交换
        变量名待优化
        """
        if k == 1:
            return head
        node = head
        first = True
        next_turn_node = None
        next_last_node = None
        last_last_node = None
        last_node = None
        while True:
            # 往下计数k个
            flag = True
            n = node
            for _ in range(k):
                if n:
                    n = n.next
                else:
                    flag = False
                    break
            if flag:
                m = k
                while m:
                    if m == k:
                        next_last_node = node
                    m -= 1
                    if m == 0:
                        if first:
                            head = node
                            first = False
                        if last_last_node:
                            last_last_node.next = node
                        last_last_node = next_last_node
                        next_turn_node = node.next
                        node.next = last_node
                        break
                    else:
                        next_node = node.next
                        node.next = last_node
                        last_node = node
                        node = next_node
                last_node = next_last_node
            else:
                last_node.next = node
                break
            node = next_turn_node
        return head

# @lc code=end
head_list = [1,2,3,4,5]
k = 4
head = None
last_node = None
for each in head_list:
    node = ListNode(each)
    if not head:
        head = node
        last_node = head
    else:
        last_node.next = node
        last_node = node
S = Solution()
ans = S.reverseKGroup(head, k)
while ans:
    print(ans.val,end=" ")
    ans = ans.next

