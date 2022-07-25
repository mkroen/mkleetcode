#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<int>> minimumAbsDifference(vector<int> &arr)
    {
        sort(arr.begin(),arr.end());
        vector<vector<int>> res;
        int n=2000000;
        for(int i=1;i<arr.size();i++){
            if (arr[i]-arr[i-1]<n){
                res.clear();
                n = arr[i]-arr[i-1];
                res.push_back({arr[i-1],arr[i]});
            }
            else if (arr[i]-arr[i-1]==n){
                res.push_back({arr[i-1],arr[i]});
            }
        }
        return res;
    }
};