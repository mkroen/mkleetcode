#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        int i = 0, len = matrix.size();
        while (i != len / 2)
        {
            swap(matrix[i], matrix[len - i - 1]);
            i++;
        }
        for (int m = 0; m < matrix.size(); m++)
        {
            for (int n = 0; n < matrix[0].size(); n++)
            {
                if (m > n)
                {
                    swap(matrix[m][n], matrix[n][m]);
                }
            }
        }
    }
};

int main()
{
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    Solution S = Solution();
    S.rotate(matrix);
    for (auto i = matrix.begin(); i != matrix.end(); i++)
    {
        for (auto j = (*i).begin(); j != (*i).end(); j++)
        {
            cout << *j << " ";
        }
        cout << endl;
    }
    return 0;
}