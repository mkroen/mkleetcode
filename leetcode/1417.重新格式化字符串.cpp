/*
 * @lc app=leetcode.cn id=1417 lang=cpp
 *
 * [1417] 重新格式化字符串
 */
#include <vector>
#include <string>
#include <stdlib.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    string reformat(string s)
    {
        vector<char> num;
        vector<char> alpha;
        for (auto &i : s)
        {
            if (isdigit(i))
            {
                num.push_back(i);
            }
            else
            {
                alpha.push_back(i);
            }
        }
        int n = num.size();
        int a = alpha.size();
        if (abs(n - a) > 1)
        {
            return "";
        }
        else
        {
            string res;
            if (n >= a)
            {
                for (int i = 0; i < n; i++)
                {
                    res += num[i];
                    if (i < a)
                    {
                        res += alpha[i];
                    }
                }
            }
            else
            {
                for (int i = 0; i < a; i++)
                {
                    res += alpha[i];
                    if (i < n)
                    {
                        res += num[i];
                    }
                }
            }
            return res;
        }
    }
};
// @lc code=end
