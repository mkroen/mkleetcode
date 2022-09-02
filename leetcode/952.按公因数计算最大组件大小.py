#
# @lc app=leetcode.cn id=952 lang=python3
#
# [952] 按公因数计算最大组件大小
#
from typing import List, Set
from collections import Counter
# @lc code=start


class UnionFind:
    # TODO 并查集
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                i += 1
        return max(Counter(uf.find(num) for num in nums).values())


def get_factors(n) -> Set[int]:
    if n == 1:
        return set()
    res = set([n])
    for i in range(2, int(n**0.5)+2):
        if n % i == 0:
            res.add(i)
            res.add(n//i)
    return res


class Solution_tle:
    def largestComponentSize(self, nums: List[int]) -> int:
        # 暴力建图 90 / 108 tle
        factors: List[Set[int]] = []
        length = len(nums)
        for n in nums:
            factors.append(get_factors(n))
        used = [False]*length
        ans = 0
        for i in range(length):
            if used[i]:
                continue
            res = 1
            l = factors[i]
            total = l.copy()
            used[i] = True
            while l:
                not_used = set()
                j = i + 1
                while j != length:
                    if used[j]:
                        j += 1
                        continue
                    if factors[j].intersection(l):
                        res += 1
                        used[j] = True
                        not_used.update(factors[j].difference(total))
                    j += 1
                l = not_used
                total.update(l)
            ans = max(res, ans)
            if ans >= used.count(False):
                break
        return ans


# @lc code=end
S = Solution()
