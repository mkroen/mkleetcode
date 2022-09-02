/*
 * @lc app=leetcode.cn id=1374 lang=cpp
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */
#include <iostream>
using namespace std;
// @lc code=start
class Solution
{
public:
    string generateTheString(int n)
    {
        if (n%2 == 0){
            string res(n-1,'a');
            res += "b";
            return res;
        }
        else{
            string res(n,'a');
            return res;
        }
    }
};
// @lc code=end

int main(){
    Solution S = Solution();
    int i = 4;
    cout<<S.generateTheString(i)<<endl;
    return 0;
}