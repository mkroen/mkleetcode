#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#
from typing import List
# @lc code=start


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 双指针解法，另可用排序 arr.sort(key=lambda v: abs(v - x))
        n = len(arr)
        for i, a in enumerate(arr):
            # 这里用二分更快
            if a >= x:
                break
        left = []
        right = []
        count = 0
        j = i - 1
        while count != k:
            if j >= 0 and i < n:
                if x-arr[j] <= arr[i]-x:
                    left.append(arr[j])
                    j -= 1
                else:
                    right.append(arr[i])
                    i += 1
            elif j < 0:
                right.append(arr[i])
                i += 1
            elif i >= n:
                left.append(arr[j])
                j -= 1
            count += 1
        left.reverse()
        return left+right


# @lc code=end
S = Solution()
print(S.findClosestElements(arr=[1, 2, 3, 4, 5], k=2, x=3))
