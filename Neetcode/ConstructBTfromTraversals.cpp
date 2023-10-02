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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> dict;
        for(int i=0; i<inorder.size(); i++){
            dict[inorder[i]] = i;
        }
        TreeNode* root = nullptr;
        int index = -1;
        for(int i=0; i<preorder.size(); i++){
            if(i==0){
                root = new TreeNode(preorder[i]);
                index = dict[preorder[i]];
            }
            else{
                int j = index;
                TreeNode* node = root;
                while(true){
                    if(dict[preorder[i]] < j){
                        if(node->left == nullptr){
                            node->left = new TreeNode(preorder[i]);
                            break;
                        }
                        else{
                            node = node->left;
                            j = dict[node->val];
                            continue;
                        }
                    }
                    else{
                        if(node->right == nullptr){
                            node->right = new TreeNode(preorder[i]);
                            break;
                        }
                        else{
                            node = node->right;
                            j = dict[node->val];
                            continue;
                        }
                    }
                }
            }
        }
        return root;
    }
};
