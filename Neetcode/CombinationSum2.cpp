class Solution {
public:
    vector<vector<int>> out;
    vector<int> res;
    void bt(vector<int> nums, int t, int i, int s){
        if (s > t || i > nums.size()){
            return;
        }
        if (s == t){
            out.push_back(res);
            return;
        }
        if (i == nums.size()){
            return;
        }
        res.push_back(nums[i]);
        bt(nums, t, i+1, s+nums[i]);
        while (i < nums.size() && nums[i] == res.back()){
            i += 1;
        }
        res.pop_back();
        bt(nums, t, i, s);
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        bt(candidates, target, 0, 0);
        return out;
    }
};
