#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """AC"""
        if numRows == 1:
            return s
        data = [[] for _ in range(numRows)]
        data_index = 0
        direction = -1
        index = 0
        max_index = len(s)
        while True:
            if index == max_index:
                break
            if data_index in (0,numRows-1):
                direction = -direction
            data[data_index].append(s[index])
            data_index += direction
            index += 1
        return "".join(["".join(each) for each in data])




# @lc code=end
s = "PAYPALISHIRING"
n=3
S = Solution()
print(S.convert(s,n))