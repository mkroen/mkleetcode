#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.l = [0]*k
        self.front = 0
        self.end = k-1
        self.last = False # 为false上一操作为delete 为true为insert

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front -= 1
        if self.front < 0:
            self.front = len(self.l) - 1
        self.l[self.front] = value
        self.last = True
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end = (self.end + 1) % len(self.l)
        self.l[self.end] = value
        self.last = True
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.l)
        self.last = False
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end -= 1
        if self.end < 0:
            self.end = len(self.l) - 1
        self.last = False
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.end]

    def isEmpty(self) -> bool:
        if self.front == (self.end+1) % len(self.l) and not self.last:
            return True
        return False

    def isFull(self) -> bool:
        if self.front == (self.end+1) % len(self.l) and self.last:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

S = MyCircularDeque(3)
print(S.insertFront(9))
print(S.getRear())
print(S.insertFront(9))
print(S.getRear())
