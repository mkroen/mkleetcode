from typing import List, Tuple
from copy import deepcopy

class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        global m, n
        n = len(chessboard)
        m = len(chessboard[0])
        for i in range(n):
            chessboard[i] = list(chessboard[i])

        def islegal(x, y):
            if 0 <= x < n and 0 <= y < m:
                return True
            return False

        def change(x, y, status: int) -> bool | Tuple[int]:
            if status == 1:
                y -= 1
            elif status == 2:
                y += 1
            elif status == 3:
                x -= 1
            elif status == 4:
                x += 1
            elif status == 5:
                x -= 1
                y += 1
            elif status == 6:
                x -= 1
                y -= 1
            elif status == 7:
                x += 1
                y += 1
            elif status == 8:
                x += 1
                y -= 1
            if islegal(x, y):
                return x, y
            else:
                return False

        def turn(x, y, cb) -> int:
            ans = 0
            if cb[x][y] == 'O':
                ans += 1
            cb[x][y] = 'X'

            for s in range(1, 9):
                i, j = x, y
                q = []
                while change(i, j, s):
                    i, j = change(i, j, s)
                    if cb[i][j] == 'X':
                        for a, b in q:
                            ans += turn(a, b, cb)
                        break
                    elif cb[i][j] == '.':
                        break
                    else:
                        q.append((i, j))
            return ans
        res = 0
        for i in range(n):
            for j in range(m):
                if chessboard[i][j] == '.':
                    res = max(res, turn(i, j, deepcopy(chessboard)))
        return res


S = Solution()
print(S.flipChess(chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]))
