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
    int height = 0;
    void dfs(TreeNode* node, int h){
        if (node == nullptr){
            height = max(height, h);
            return;
        }
        dfs(node->left, h+1);
        dfs(node->right, h+1);
    }
    int maxDepth(TreeNode* root) {
        dfs(root, 0);
        return height;
    }
};
