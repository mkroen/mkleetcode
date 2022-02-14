class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

# 执行用时：316 ms, 在所有 Python3 提交中击败了93.29%的用户
# 内存消耗：18.7 MB, 在所有 Python3 提交中击败了28.08%的用户
# 通过测试用例：55 / 55