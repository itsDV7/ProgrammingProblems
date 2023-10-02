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
    vector<int> inord;
    void bt(TreeNode* node){
        if(node == nullptr){
            return;
        }
        bt(node->left);
        inord.push_back(node->val);
        bt(node->right);
    }
    int kthSmallest(TreeNode* root, int k) {
        bt(root);
        return inord[k-1];
    }
};
