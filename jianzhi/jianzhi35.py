"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 骚操作↓

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         from copy import deepcopy
#         # python 就是屌
#         return deepcopy(head)


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        head_list = []
        while head:
            head_list.append(head)
            head = head.next # type: ignore
        head_new = [Node(0) for _ in head_list]
        for index, each in enumerate(head_list):
            head_new[index].val = each.val
            if each.next:
                head_new[index].next = head_new[head_list.index(each.next)]
            if each.random:
                head_new[index].random = head_new[head_list.index(each.random)]
        return head_new[0]

# 执行用时：36 ms, 在所有 Python3 提交中击败了71.19%的用户
# 内存消耗：15.6 MB, 在所有 Python3 提交中击败了85.81%的用户
# 通过测试用例：18 / 18