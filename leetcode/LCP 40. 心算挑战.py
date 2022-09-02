from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        a, b = [], []
        for c in cards:
            if c % 2 == 1:
                a.append(c)
            else:
                b.append(c)
        a.sort(reverse=True)
        b.sort(reverse=True)
        al, bl = len(a), len(b)
        for i in range(1, al):
            a[i] += a[i-1]
        a = [0] + a
        for i in range(1, bl):
            b[i] += b[i-1]
        b = [0] + b
        res = [0]
        i = cnt-bl  # 奇数个数
        if i < 0:
            i = 0
        elif i % 2 == 1:
            i += 1
        while i <= cnt and i <= al and cnt-i <= bl:
            res.append(a[i]+b[cnt-i])
            i += 2
        return max(res)


S = Solution()
print(S.maxmiumScore(cards=[7, 6, 4, 6], cnt=1))
