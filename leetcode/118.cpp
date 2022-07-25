#include <iostream>
#include <vector>

using namespace std;
class Solution
{
public:
    vector<vector<int>> generate(int numRows)
    {
        vector<vector<int>> res;
        vector<int> v = {1};
        vector<int> n;
        res.push_back(v);
        for (int i = 1; i < numRows; i++)
        {
            n = {1};
            for (int j = 1; j < i; j++)
            {
                n.push_back(v[j] + v[j - 1]);
            }
            n.push_back(1);
            res.push_back(n);
            v = n;
        }
        return res;
    }
};