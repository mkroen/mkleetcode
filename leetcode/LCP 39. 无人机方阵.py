from typing import List
from collections import Counter

class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        res = Counter()
        for s in source:
            res += Counter(s)
        for t in target:
            res -= Counter(t)
        return sum(res.values())