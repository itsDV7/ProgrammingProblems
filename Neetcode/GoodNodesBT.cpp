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
    int count = 0;
    void bt(TreeNode* node, int maxH){
        if(node == nullptr){
            return;
        }
        if(node->val >= maxH){
            count += 1;
            maxH = max(maxH, node->val);
        }
        bt(node->left, maxH);
        bt(node->right, maxH);
    }
    int goodNodes(TreeNode* root) {
        bt(root, root->val);
        return count;
    }
};
