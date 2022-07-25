#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 数学方法 一共m+n-2步 选m-1步向下
        def cmn(m, n):
            res = 1
            if n > m//2:
                n = m-n
            for i in range(n):
                res *= (m-i)
                res //= (i+1)
            return res
        return cmn(m+n-2, m-1)

    def uniquePaths_v3(self, m: int, n: int) -> int:
        # dp
        dp = [[1]*m] + [[1] + [0]*(m-1) for _ in range(n-1)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths_v2(self, m: int, n: int) -> int:
        # dfs超时
        res = 0

        def dfs(x, y):
            if x == m and y == n:
                nonlocal res
                res += 1
            else:
                if x != m:
                    dfs(x+1, y)
                if y != n:
                    dfs(x, y+1)
        dfs(1, 1)
        return res

# @lc code=end


S = Solution()
print(S.uniquePaths(m=3, n=7))
print(S.uniquePaths(m=23, n=12))
