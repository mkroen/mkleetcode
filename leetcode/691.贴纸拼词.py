#
# @lc app=leetcode.cn id=691 lang=python3
#
# [691] 贴纸拼词
#
from typing import List

# @lc code=start


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        "tle"
        ans = 0
        alpha_map = {}
        alpha_count = {}
        target_count = {}
        for t in target:
            target_count[t] = target_count.get(t, 0) + 1
        for s in stickers:
            for a in s:
                if not alpha_count.get(s):
                    alpha_count[s] = {}
                alpha_count[s][a] = alpha_count[s].get(a, 0) + 1
                if not alpha_map.get(a):
                    alpha_map[a] = []
                alpha_map[a].append(s)

        print(alpha_map)

        def find(target_count: dict, now=0):
            nonlocal ans, alpha_map, alpha_count
            if ans == -1:
                return
            if not target_count:
                ans = min(now, ans) if ans else now
                return
            alpha = list(target_count.keys())[0]
            choose = alpha_map.get(alpha)
            if not choose:
                ans = -1
                return
            for c in choose:
                target = target_count.copy()
                m = alpha_count[c]
                for k, v in m.items():
                    if k not in target:
                        continue
                    else:
                        target[k] -= v
                        if target[k] <= 0:
                            target.pop(k)
                find(target, now+1)
        find(target_count)
        return ans or -1

    def minStickers_v2(self, stickers: List[str], target: str) -> int:
        # 考虑的是需要按顺序，不能剪成最小的字母
        ans = 0
        alpha_map = {}
        for s in stickers:
            for i in range(len(s)):
                for l in range(1, len(s)-i+1):
                    if not alpha_map.get(s[i]):
                        alpha_map[s[i]] = set()
                    alpha_map[s[i]].add(s[i:i+l])

        def find(remain, now=0):
            nonlocal ans, alpha_map
            print(ans, remain, now)
            if ans == -1:
                return
            if remain == "":
                ans = min(now, ans) if ans else now
            for i in range(1, len(remain)+1):
                if not alpha_map.get(remain[0]):
                    ans = -1
                    return
                if remain[:i] in alpha_map[remain[0]]:
                    find(remain[i:], now+1)
                else:
                    break
        find(target)
        return ans or -1


S = Solution()
stickers = ["control", "heart", "interest", "stream", "sentence", "soil", "wonder", "them", "month", "slip", "table", "miss", "boat", "speak", "figure", "no", "perhaps", "twenty", "throw", "rich", "capital", "save", "method",
            "store", "meant", "life", "oil", "string", "song", "food", "am", "who", "fat", "if", "put", "path", "come", "grow", "box", "great", "word", "object", "stead", "common", "fresh", "the", "operate", "where", "road", "mean"]
target = "stoodcrease"
print(S.minStickers(stickers, target))

# @lc code=end
