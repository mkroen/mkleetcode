#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int last = 0, res = nums[0];
        for (auto const &n : nums)
        {
            res = max(res, last + n);
            last = max(n + last, n);
        }
        return res;
    }
};

class Solution2
{
    // 分治法
public:
    struct Status
    {
        int lSum, rSum, mSum, iSum;
    };

    Status pushUp(Status l, Status r)
    {
        int iSum = l.iSum + r.iSum;
        int lSum = max(l.lSum, l.iSum + r.lSum);
        int rSum = max(r.rSum, r.iSum + l.rSum);
        int mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum);
        return (Status){lSum, rSum, mSum, iSum};
    };

    Status get(vector<int> &a, int l, int r)
    {
        if (l == r)
        {
            return (Status){a[l], a[l], a[l], a[l]};
        }
        int m = (l + r) >> 1;
        Status lSub = get(a, l, m);
        Status rSub = get(a, m + 1, r);
        return pushUp(lSub, rSub);
    }

    int maxSubArray(vector<int> &nums)
    {
        return get(nums, 0, nums.size() - 1).mSum;
    }
};