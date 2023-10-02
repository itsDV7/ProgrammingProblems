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
    vector<int> s;

    void lrri(TreeNode* node){
            if (node == nullptr){
                return;
            }
            lrri(node->left);
            s.push_back(node->val);
            lrri(node->right);
        }
    
    bool isValidBST(TreeNode* root) {
        lrri(root);
        for (int i=1; i<s.size(); i++){
            if (s[i-1] >= s[i]){
                return false;
            }
        }
        return true;
    }
};
