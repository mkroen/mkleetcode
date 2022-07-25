#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.l = []

    def book(self, start: int, end: int) -> bool:
        # O(n2) 此题还可以用二分搜索或者线段树
        for (s, e) in self.l:
            if s <= start < e or s < end <= e or (start < s and end > e):
                return False
        self.l.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end
