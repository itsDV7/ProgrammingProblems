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
    bool balance = true;
    int bt(TreeNode* node){
        if (node == nullptr){
            return 0;
        }
        int left = bt(node->left);
        int right = bt(node->right);
        balance = balance && (abs(left - right) <= 1);
        return 1 + max(left, right);
    }
    bool isBalanced(TreeNode* root) {
        bt(root);
        return balance;
    }
};
