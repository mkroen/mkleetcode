from typing import List
from bisect import bisect_left
from collections import defaultdict


class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:
        keys = set()
        values = defaultdict(list)
        for a, b in circles:
            values[a].append(b)
            keys.add(a)
        keys = list(keys)
        keys.sort()
        for k in keys:
            values[k].sort()
        n = len(keys)
        res = 0
        for a, b, rr in toys:
            i = bisect_left(keys, a-r)
            flag = True
            while i < n and flag:
                x = keys[i]
                if x > a+r:
                    break
                v = values[x]
                j = bisect_left(v, b-r)
                m = len(v)
                while j < m:
                    y = v[j]
                    if y > b+r:
                        break
                    if r < rr:
                        j += 1
                        continue
                    if (x-a)**2+(y-b)**2 <= (r-rr)**2:
                        res += 1
                        flag = False
                        break
                    j += 1
                i += 1
        return res
