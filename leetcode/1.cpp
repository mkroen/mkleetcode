#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i)
        {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end())
            {
                return {it->second, i};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};

class Solution2
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            int need = target - nums[i];
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[j] == need)
                {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
int main()
{
    return 0;
}