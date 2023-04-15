class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numset;
        int count = 0, ans=0;
        for (int n:nums){
            numset.insert(n);
        }
        for(int n:nums){
            count += 1;
            if (numset.count(n-1) == 0){
                while (numset.count(n+1) != 0){
                    count += 1;
                    n += 1;
                }
            }
            ans = max(count, ans);
            count = 0;
        }
        return ans;
    }
};
