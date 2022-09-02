#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from typing import List
# @lc code=start


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        l = []
        i = j = 0
        while True:
            if j == n:
                break
            if l and l[-1] == popped[j]:
                j += 1
                l.pop()
            elif i != n:
                l.append(pushed[i])
                i += 1
            else:
                return False
        return True


# @lc code=end
S = Solution()
print(S.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))