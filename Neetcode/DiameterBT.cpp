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
    int diameter = 0;
    int bt(TreeNode* node){
        if (node == nullptr){
            return -1;
        }
        int left = bt(node->left);
        int right = bt(node->right);
        diameter = max(diameter, left + right + 2);
        return 1 + max(left, right);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        bt(root);
        return diameter;
    }
};
