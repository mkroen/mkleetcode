from typing import List
from collections import deque


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # 拓扑排序思想 👍
        d = {}
        n = len(nums)
        in_d = [-1] + [0] * n
        for each in sequences:
            for i in range(1, len(each)):
                a, b = each[i-1], each[i]
                if not d.get(a):
                    d[a] = []
                d[a].append(b)
                in_d[b] += 1
        q = deque([i for i, v in enumerate(in_d) if v == 0])
        while q:
            if len(q) > 1:
                return False
            x = q.popleft()
            for each in d.get(x, []):
                in_d[each] -= 1
                if in_d[each] == 0:
                    q.append(each)
        return True


S = Solution()
print(S.sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2]]))
