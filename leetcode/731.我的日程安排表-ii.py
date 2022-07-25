#
# @lc app=leetcode.cn id=731 lang=python3
#
# [731] 我的日程安排表 II
#
from re import T
from typing import List
# @lc code=start


class MyCalendarTwo:

    def __init__(self):
        self.l = []
        self.d = []

    def book(self, start: int, end: int) -> bool:
        dd = []
        for a,b in self.l:
            flag = False
            if a<=start<b and a<end<=b:
                flag = True
                m,n = start,end
            elif a<=start<b:
                flag = True
                m,n = start,b
            elif a<end<=b:
                flag = True
                m,n = a,end
            elif start<=a and b<=end:
                flag = True
                m,n = a,b
            if flag:
                for c,d in self.d:
                    if c<=m<d or c<n<=d or (m<c and n>d):
                        return False
                dd.append((m,n))
        self.d += dd
        self.l.append((start,end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end
