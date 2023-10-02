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
    int maxH = -1;
    vector<int> view;
    void bt(TreeNode* node, int h){
        if (node == nullptr){
            return;
        }
        if (h > maxH){
            view.push_back(node->val);
            maxH = h;
        }
        bt(node->right, h+1);
        bt(node->left, h+1);
    }
    vector<int> rightSideView(TreeNode* root) {
        bt(root, 0);
        return view;
    }
};
