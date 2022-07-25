#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> count1(1001), count2(1001);
        for (int i = 0; i < nums1.size(); i++)
        {
            count1[nums1[i]]++;
        }
        for (int i = 0; i < nums2.size(); i++)
        {
            count2[nums2[i]]++;
        }
        vector<int> res;
        for (int i = 0; i < 1001; i++)
        {
            for (int j = 0; j < min(count1[i], count2[i]); j++)
            {
                res.push_back(i);
            }
        }
        return res;
    }
};