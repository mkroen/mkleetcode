class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if len(self.min_stack) != 0:
            self.stack.append(x)
            if self.min_stack[-1] < x:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(x)
        else:
            self.stack.append(x)
            self.min_stack.append(x)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

# 执行用时：56 ms, 在所有 Python3 提交中击败了56.46%的用户
# 内存消耗：18.5 MB, 在所有 Python3 提交中击败了5.59%的用户
# 通过测试用例：19 / 19