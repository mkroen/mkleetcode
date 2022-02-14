class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return "".join((s[n:], s[0:n]))

# 执行用时：32 ms, 在所有 Python3 提交中击败了73.00%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了99.33%的用户
# 通过测试用例：34 / 34