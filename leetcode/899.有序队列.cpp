/*
 * @lc app=leetcode.cn id=899 lang=cpp
 *
 * [899] 有序队列
 */
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution
{
public:
    string orderlyQueue(string s, int k)
    {
        if (k == 1)
        {
            s += s;
            string_view sv(s), ans(sv);
            for (int i = 0, n = s.size() / 2; i < n; i++)
            {
                ans = min(ans, sv.substr(i, n));
            }
            return {ans.cbegin(), ans.cend()};
        }
        else
        {
            sort(s.begin(), s.end());
            return s;
        }
    }
};
// @lc code=end
