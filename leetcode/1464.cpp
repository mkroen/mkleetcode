/*
 * @lc app=leetcode.cn id=1464 lang=cpp
 *
 * [1464] 数组中两元素的最大乘积
 */
#include <vector>
#include <iostream>
using namespace std;
// @lc code=start
class Solution
{
public:
    int maxProduct(vector<int> &nums)
    {
        int i = 0, j = 0;
        for (int n : nums)
        {
            if (n > i)
            {
                i = n;
                if (i > j)
                {
                    swap(i, j);
                }
            }
        }
        return (i - 1) * (j - 1);
    }
};
// @lc code=end
int main()
{
    Solution S = Solution();
    vector<int> v = {3, 4, 5, 2};
    cout << S.maxProduct(v);
    return 0;
}