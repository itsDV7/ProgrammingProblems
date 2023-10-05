class Solution {
public:
    vector<vector<int>> out;
    vector<int> res;
    void bt(vector<int> nums){
        if (res.size() == nums.size()){
            out.push_back(res);
            return;
        }
        for(int i=0; i<nums.size(); i++){
            if(find(res.begin(), res.end(), nums[i]) == res.end()){
                res.push_back(nums[i]);
                bt(nums);
                res.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        bt(nums);
        return out;
    }
};
