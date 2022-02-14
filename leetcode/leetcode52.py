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

# 执行用时：56 ms, 在所有 Python3 提交中击败了42.55%的用户
# 内存消耗：22.4 MB, 在所有 Python3 提交中击败了5.42%的用户
# 通过测试用例：9 / 9

# 算出来提交↓

# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         return {1:1,2:0,3:0,4:2,5:10,6:4,7:40,8:92,9:352}.get(n) # type: ignore
# 执行用时：28 ms, 在所有 Python3 提交中击败了99.28%的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了96.12%的用户
# 通过测试用例：9 / 9