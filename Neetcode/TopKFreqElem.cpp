class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> count;
        for (int n: nums){
            count[n]++;
        }
        struct ValueComparator{
            bool operator()(const pair<int, int> &a, const pair<int, int> &b) const {
                return a.second < b.second;
            }
        };

        priority_queue<pair<int, int>, vector<pair<int, int>>, ValueComparator> pq;
        for(auto p: count){
            pq.push(p);
        }

        vector<int> ans;
        for(int i=0; i<k; i++){
            ans.push_back(pq.top().first);
            pq.pop();
        }

        return ans;
    }
};
