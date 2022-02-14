class Solution:
    def replaceSpace(self, s: str) -> str:
        return "%20".join(s.split(" "))

# 执行用时：28 ms, 在所有 Python3 提交中击败了84.48%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了50.52%的用户
# 通过测试用例：27 / 27