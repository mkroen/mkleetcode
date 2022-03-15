#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        class setdata:
            def __init__(self, set1: set, set2: set, set3: set):
                self.set1 = set1
                self.set2 = set2
                self.set3 = set3
            # def __str__(self):
            #     return f"{self.set1},{self.set2},{self.set3}"
        
        # ↓line, ↘diff, ↗diff
        data = setdata(set(), set(), set())
        turns = [data]
        for i in range(n):
            # 第几轮 
            new_turn = []
            for turn in turns:
                for j in range(n):
                    # 第几列
                    if j not in turn.set1 and j-i not in turn.set2 and i+j not in turn.set3:
                        # newdata = deepcopy(turn)
                        # newdata.set1.add(j)
                        # newdata.set2.add(j-i)
                        # newdata.set3.add(j+i)
                        # new_turn.append(newdata)
                        newset1 = set().union(turn.set1)
                        newset2 = set().union(turn.set2)
                        newset3 = set().union(turn.set3)
                        newset1.add(j)
                        newset2.add(j-i)
                        newset3.add(i+j)
                        new_turn.append(setdata(newset1, newset2, newset3))                        
            turns = new_turn
        return len(turns)
# @lc code=end

