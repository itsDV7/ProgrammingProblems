class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int K) {
        vector<int> max_ans;
        deque<int> Qi;
        int i=0;
        int N=nums.size();
        for (i = 0; i < K; ++i) {
            while ((!Qi.empty()) && nums[i] >= nums[Qi.back()])
                Qi.pop_back();
            Qi.push_back(i);
        }
        for (i=K; i < N; ++i) {
            max_ans.push_back(nums[Qi.front()]);
            //cout << i - K;
            while ((!Qi.empty()) && Qi.front() <= i - K)
                Qi.pop_front();
            while ((!Qi.empty()) && nums[i] >= nums[Qi.back()])
                Qi.pop_back();
            Qi.push_back(i);
        }
        max_ans.push_back(nums[Qi.front()]);
        return max_ans;
    }
};
