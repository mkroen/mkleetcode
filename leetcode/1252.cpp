#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int oddCells(int m, int n, vector<vector<int>> &indices)
    {
        vector<int> ml(m), nl(n);
        for (auto const &tuple : indices)
        {
            ml[tuple[0]]++;
            nl[tuple[1]]++;
        }
        int res = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                res += (ml[i] + nl[j]) % 2;
            }
        }
        return res;
    }
};