#include <iostream>
#include <vector>

using namespace std;

void print(vector<vector<int>> &matrix)
{
    for (int i = 0; i < matrix.size(); i++)
    {
        for (auto j = matrix[i].begin(); j != matrix[i].end(); j++)
        {
            cout << *j << " ";
        }
        cout << endl;
    }
    cout << endl;
}

class Solution
{
public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        int col = matrix[0].size();
        int row = matrix.size();
        bool flag = false;
        for (int j = 0; j < col; j++)
        {
            if (matrix[0][j] == 0)
            {
                flag = true;
                break;
            }
        }
        for (int i = 1; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        print(matrix);
        for (int i = 1; i < row; i++)
        {
            if (matrix[i][0] == 0)
            {
                for (int j = 1; j < col; j++)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        print(matrix);
        for (int j = 0; j < col; j++)
        {
            if (matrix[0][j] == 0)
            {
                for (int i = 1; i < row; i++)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        print(matrix);
        if (flag)
        {
            for (int j = 0; j < col; j++)
            {
                matrix[0][j] = 0;
            }
        }
        print(matrix);
    }
};

int main()
{
    // vector<vector<int>> matrix = {{-4, -2147483648, 6, -7, 0}, {-8, 6, -8, -6, 0}, {2147483647, 2, -9, -6, -10}};
    vector<vector<int>> matrix = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    print(matrix);
    Solution S = Solution();
    S.setZeroes(matrix);
    return 0;
}