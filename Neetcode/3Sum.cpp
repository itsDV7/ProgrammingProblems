#include <algorithm>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l, r, sm;
        vector<vector<int>> ans;
        for (int i=0; i<nums.size(); i++){
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }

            l = i + 1;
            r = nums.size() - 1;

            while (l < r){
                sm = nums[i] + nums[l] + nums[r];
                if (sm > 0){
                    r -= 1;
                }
                else if (sm < 0){
                    l += 1;
                }
                else{
                    ans.push_back({nums[i], nums[l], nums[r]});
                    l += 1;
                    while (nums[l] == nums[l-1] && l < r){
                        l += 1;
                    }
                }
            }
        }
        return ans;
    }
};
