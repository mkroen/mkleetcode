class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def count(num1: int, num2: int) -> int:
            res = 0
            for num in (num1, num2):
                while True:
                    res += num%10
                    num = num//10
            return res
        if n > m:
            m, n = n, m
        ans = 0
        d = dict()
        for i in range(m):
            for j in range(n):
                if j > i:
                    ans += d[(j, i)]
                else:
                    d[(i, j)] = count(i, j)
                    ans += d[(i, j)]
        return ans