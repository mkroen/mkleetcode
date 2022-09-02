/*
 * @lc app=leetcode.cn id=1282 lang=cpp
 *
 * [1282] 用户分组
 */
#include <iostream>
#include <vector>
#include <map>
using namespace std;
// @lc code=start
class Solution
{
public:
    vector<vector<int>> groupThePeople(vector<int> &groupSizes)
    {
        map<int, vector<int>> m;
        for (int i = 0; i < groupSizes.size(); ++i)
        {
            if (m.find(groupSizes[i]) != m.end())
            {
                m[groupSizes[i]].push_back(i);
            }
            else
            {
                m[groupSizes[i]] = vector<int>{i};
            }
        }
        vector<vector<int>> res;
        for (auto it = m.begin(); it != m.end(); it++)
        {
            int i = 0;
            while (true)
            {
                if (i < it->second.size())
                {
                    res.push_back({it->second.begin() + i, it->second.begin() + i + it->first});
                    i += it->first;
                }
                else
                {
                    break;
                }
            }
        }
        return res;
    }
};
// @lc code=end

int main()
{
    vector<int> g = {3, 3, 3, 3, 3, 1, 3};
    Solution S = Solution();
    vector<vector<int>> res = S.groupThePeople(g);
    for (vector<int> v : res)
    {
        for (int n : v)
        {
            cout << n << "";
        }
        cout << endl;
    }
    return 0;
}