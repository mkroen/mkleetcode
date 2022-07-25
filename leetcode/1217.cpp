#include <iostream>
#include <vector>

using namespace std;
class Solution
{
public:
    int minCostToMoveChips(vector<int> &position)
    {
        int a = 0, b = 0;
        for (auto i = position.begin(); i != position.end(); i++)
        {
            if (*i % 2 == 1)
                a++;
            else
                b++;
        }
        return min(a, b);
    }
};