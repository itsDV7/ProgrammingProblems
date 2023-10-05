class Solution {
public:
    vector<vector<int>> out;
    vector<int> res;
    void bt(vector<int> nums, int i){
        if (i >= nums.size()){
            out.push_back(res);
            return;
        }
        res.push_back(nums[i]);
        bt(nums, i+1);
        res.pop_back();
        bt(nums, i+1);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        bt(nums, 0);
        return out;
    }
};
