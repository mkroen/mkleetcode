#include <iostream>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution
{
public:
    int firstUniqChar(string s)
    {
        unordered_map<char, int> hash;
        unordered_set<char> set;
        for (int i = 0; i < s.length(); i++)
        {
            if (set.find(s[i]) == set.end())
            {
                if (hash.find(s[i]) == hash.end())
                {
                    hash.emplace(s[i], i);
                    cout << "insert  " << s[i] << " " << i << endl;
                }
                else
                {
                    hash.erase(s[i]);
                    set.insert(s[i]);
                    cout << "erase  " << s[i] << endl;
                }
            }
        }
        int res = -1;
        if (!hash.empty()){
            res = hash.begin()->second;
        }
        // for (auto it = hash.begin(); it != hash.end(); it++)
        // {
        //     cout << it->first << it->second << endl;
        // }
        return res;
    }
};

int main()
{
    Solution S = Solution();
    string s = "loveleetcode";
    int res = S.firstUniqChar(s);
    cout << "ans" << res << endl;
    return 0;
}