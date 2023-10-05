class Solution {
public:
    vector<vector<int>> out;
    vector<int> res;
    void bt(vector<int> nums, int i){
        if (i > nums.size()){
            return;
        }
        if (i == nums.size()){
            out.push_back(res);
            return;
        }
        res.push_back(nums[i]);
        bt(nums, i+1);
        while (i < nums.size() && nums[i] == res.back()){
            i += 1;
        }
        res.pop_back();
        bt(nums, i);
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        bt(nums, 0);
        return out;
    }
};
