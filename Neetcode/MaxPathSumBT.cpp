/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res = -1001;
    int bt(TreeNode* node){
        if(node == nullptr){
            return 0;
        }
        int left = bt(node->left);
        int right = bt(node->right);
        res = max({res, node->val, node->val + max(left, right), node->val + left + right});
        return max({0, node->val, node->val + max(left, right)});
    }
    int maxPathSum(TreeNode* root) {
        bt(root);
        return res;
    }
};
