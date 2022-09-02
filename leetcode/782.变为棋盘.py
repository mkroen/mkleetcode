#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#
from typing import List
# @lc code=start


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(1, n):
            flag = board[i][0] == board[0][0]
            for j in range(1, n):
                if (board[i][j] == board[0][j]) != flag:
                    return -1
        flag = n % 2
        if not flag:
            # 偶数
            for i in range(n):
                if board[i].count(0) * 2 != n:
                    return -1
                if sum([board[j][i] == 0 for j in range(n)])*2 != n:
                    return -1
            ans1, ans2 = 0, 0
            col = [board[i][0] for i in range(n)]
            for i in range(n):
                if i % 2 != board[0][i]:
                    ans1 += 1
                if i % 2 != col[i]:
                    ans2 += 1
            return (min(ans1, n-ans1)+min(ans2, n-ans2))//2
        else:
            # 奇数
            col = [board[i][0] for i in range(n)]
            status = [board[i].count(1) > board[i].count(0) for i in range(n)]
            c = status.count(1)
            if c*2-1 == n:
                val = 1
            elif c*2+1 == n:
                val = 0
            else:
                return -1
            raw = []
            for i in range(n):
                s = [board[j][i] for j in range(n)]
                raw.append(s.count(1) > s.count(0))
            if not (raw.count(1)*2-1 == n and val == 1) and not (raw.count(1)*2+1 == n and val == 0):
                return -1
            ans = 0
            val1 = board[0].count(1) > board[0].count(0)
            val2 = col.count(1) > col.count(0)
            for i in range(n):
                if (val1+i) % 2 != board[0][i]:
                    ans += 1
                if (val2+i) % 2 != col[i]:
                    ans += 1
            return ans // 2


# @lc code=end


S = Solution()
print(S.movesToChessboard(
    [[0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0]]))
