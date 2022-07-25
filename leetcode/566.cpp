#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> matrixReshape(vector<vector<int>> &mat, int r, int c)
    {
        int row = mat.size(), col = mat[0].size();
        if (r * c != col * row)
            return mat;
        vector<vector<int>> res(r, vector<int>(c));
        int count = 0;
        vector<int> v;
        for(int i=0; i < r*c; i++){
            res[i/c][i%c] = mat[i/col][i%col];
        }
        return res;
    }
};