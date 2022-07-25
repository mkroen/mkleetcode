#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int i = m - 1, j = n - 1, last = m + n - 1;
        while (j != -1)
        {
            if (i == -1)
            {
                nums1[j] = nums2[j];
                j--;
                continue;
            }
            if (nums1[i] > nums2[j])
            {
                nums1[last--] = nums1[i--];
            }
            else
            {
                nums1[last--] = nums2[j--];
            }
        }
    }
    void merge_v2(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        // violence
        for (int i = 0; i < n; i++)
        {
            nums1[i + m] = nums2[i];
        }
        sort(nums1.begin(), nums1.end());
    }
};

int main()
{
    vector<int> a = {2, 0}, b = {1};
    int m = 1, n = 1;
    Solution S = Solution();
    S.merge(a, m, b, n);
    for (int i = 0; i < a.size(); i++)
    {
        cout << a[i] << endl;
    }
}