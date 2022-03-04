#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """使用n+1长度的队列，取前三个，删除第二个, 一趟扫描，内存最优"""
        from queue import Queue
        q = Queue(maxsize=n+1)
        q.put(head)
        node = head.next
        while node:
            if q.full():
                q.get()
            q.put(node)
            node = node.next
        if not q.full():
            return head.next # type: ignore
        a = q.get()
        q.get()
        c = q.get() if not q.empty() else None
        a.next = c
        return head

# @lc code=end
S = Solution()
head_list = [1, 2]
n = 1
head = ListNode(head_list[0])
node = head
for i in head_list[1:]:
    node.next = ListNode(i)
    node = node.next
L = S.removeNthFromEnd(head, n)
while L:
    print(L.val)
    L = L.next
