/*
 * @lc app=leetcode.cn id=1302 lang=cpp
 *
 * [1302] 层数最深叶子节点的和
 */
#include <vector>
using namespace std;
// @lc code=start
// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution
{
public:
    int deepestLeavesSum(TreeNode *root)
    {
        vector<TreeNode *> t = {root};
        vector<TreeNode *> n;
        int res;
        while (!t.empty()){
            res = 0;
            n.clear();
            for(auto i: t){
                if(i != nullptr){
                    res += i->val;
                    if(i->left!=nullptr){
                        n.push_back(i->left);
                    }
                    if(i->right!=nullptr){
                        n.push_back(i->right);
                    }
                }
            }
            t = n;
        }
        return res;
    }
};
// @lc code=end
