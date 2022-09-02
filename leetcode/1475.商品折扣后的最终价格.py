#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#
from typing import List
# @lc code=start


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 单调栈
        n = len(prices)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            temp = prices[i]
            prices[i] -= stack[-1] if stack else 0
            stack.append(temp)
        return prices

    def finalPrices_v2(self, prices: List[int]) -> List[int]:
        # on2遍历
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices


# @lc code=end
S = Solution()
print(S.finalPrices(prices=[8, 4, 6, 2, 3]))
