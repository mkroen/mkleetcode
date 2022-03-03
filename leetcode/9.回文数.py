#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ac,给了个数组存,不给也可以实现,但速度应该会慢一些
        正常逻辑直接转字符串处理
        """
        if x<0:
            return False
        elif x<10:
            return True
        l = []
        while x:
            l.append(x%10)
            x = x//10
        count = len(l)
        flag = True
        for i in range(count//2):
            if l[i] != l[-i-1]:
                flag = False
                break
        return flag
    
    def isPalindrome_v2(self, x: int) -> bool:
        """7755/11510 cases passed (N/A)
        1000021 拿不到0
        """
        def fun(n):
            i = 1
            while n>i:
                i*=10
            return i/10
        if x<0:
            return False
        elif x<10:
            return True
        flag = True
        while x>=10:
            base = fun(x)
            left = x//base
            right = x%10
            if left!=right:
                flag = False
                break
            x = x%base //10 # type:ignore
        return flag



# @lc code=end

S = Solution()
n = 100000000000000021
print(S.isPalindrome(n))