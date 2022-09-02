/*
 * @lc app=leetcode.cn id=1413 lang=cpp
 *
 * [1413] 逐步求和得到正数的最小值
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    int minStartValue(vector<int> &nums)
    {
        int m = nums[0];
        int total = 0;
        for (int i : nums)
        {
            total += i;
            m = min(total, m);
        }
        return m < 0 ? (-m + 1) : 1;
    }
};
// @lc code=end
