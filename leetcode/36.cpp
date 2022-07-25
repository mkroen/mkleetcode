#include <iostream>
#include <vector>
#include <set>

using namespace std;
class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        set<int> row_set, col_set;
        for (int i = 0; i < 9; i++)
        {
            row_set.clear();
            col_set.clear();
            for (int j = 0; j < 9; j++)
            {
                if ((board[i][j] != '.') && (row_set.count(board[i][j])))
                {
                    return false;
                }
                else if (board[i][j] != '.')
                {
                    row_set.insert(board[i][j]);
                }
                if ((board[j][i] != '.') && (col_set.count(board[j][i])))
                {
                    return false;
                }
                else if (board[j][i] != '.')
                {
                    col_set.insert(board[j][i]);
                }
            }
        }

        for (int a = 0; a < 3; a++)
        {
            for (int b = 0; b < 3; b++)
            {
                row_set.clear();
                for (int m = 0; m < 3; m++)
                {
                    for (int n = 0; n < 3; n++)
                    {
                        if ((board[m + 3 * a][n + 3 * b] != '.') && (row_set.count(board[m + 3 * a][n + 3 * b])))
                        {
                            return false;
                        }
                        else if (board[m + 3 * a][n + 3 * b] != '.')
                        {
                            row_set.insert(board[m + 3 * a][n + 3 * b]);
                        }
                    }
                }
            }
        }
        return true;
    }
};