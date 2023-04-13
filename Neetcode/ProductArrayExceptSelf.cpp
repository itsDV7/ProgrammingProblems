class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int nsize = nums.size();
        vector<int> ans(nsize, 1);
        int f(1), r(1);
        // cout << nsize << "\n";
        for (int i=0; i<nsize; i++){
            if (i!=0){
                f *= nums[i-1];
                ans[i] *= f;
            }
            if (nsize-1-i != nsize-1){
                r *= nums[nsize-i];
                ans[nsize-1-i] *= r;
            }
            // cout << i << " " << ans[i] << " " << nsize-1-i << " " << ans[nsize-1-i] << "\n";
        }
        return ans;
    }
};
