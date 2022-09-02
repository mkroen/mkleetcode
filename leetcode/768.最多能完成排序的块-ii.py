#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#
from typing import List
# @lc code=start


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        min_index = [0]*n
        for i in range(n):
            index = -1
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    index = j
            min_index[i] = index
        res = 0
        i = 0
        while i < n:
            res += 1
            if min_index[i] == -1:
                i += 1
            else:
                j = min_index[i]
                while j < max(min_index[i:j+1]):
                    j = max(min_index[i:j+1])
                i = j+1
        return res


class Solution2:
    # lc 单调栈解法
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for a in arr:
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
        return len(stack)

# @lc code=end


S = Solution()
print(S.maxChunksToSorted(arr=[0, 3, 0, 3, 2]))
