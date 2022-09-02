/*
 * @lc app=leetcode.cn id=1403 lang=cpp
 *
 * [1403] 非递增顺序的最小子序列
 */
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
// @lc code=start
class Solution
{
public:
    vector<int> minSubsequence(vector<int> &nums)
    {
        sort(nums.rbegin(), nums.rend());
        int total = accumulate(nums.begin(), nums.end(), 0);
        int count = 0;
        vector<int> res;
        for (int i = 0; i != nums.size(); ++i)
        {
            count += nums[i];
            if (count>total-count){
                res.assign(nums.begin(),nums.begin()+i+1);
                break;
            }
        }
        return res;
    }
};
// @lc code=end
