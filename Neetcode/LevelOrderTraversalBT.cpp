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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> output;
        deque<TreeNode*> res;
        if(root == nullptr){
            return {};
        }
        res.push_back(root);
        while (!res.empty()){
            vector<int> vals;
            int i = res.size();
            for(int j=0; j<i; j++){
                if(res[j]->left != nullptr){
                    res.push_back(res[j]->left);
                }
                if(res[j]->right != nullptr){
                    res.push_back(res[j]->right);
                }
            }
            for(int j=0; j<i; j++){
                vals.push_back(res[j]->val);
            }
            for(int j=0; j<i; j++){
                res.pop_front();
            }
            output.push_back(vals);
        }
        return output;
    }
};
