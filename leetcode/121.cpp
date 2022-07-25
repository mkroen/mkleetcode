#include <iostream>
#include <vector>

using namespace std;
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int small = 100001, res = 0;
        for (int i = 0; i < prices.size(); i++)
        {
            if (prices[i] - small > res)
                res = prices[i] - small;
            if (prices[i] < small)
                small = prices[i];
        }
        return res;
    }
};