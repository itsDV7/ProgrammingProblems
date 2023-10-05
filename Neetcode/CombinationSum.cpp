class Solution {
public:
    vector<vector<int>> out;
    vector<int> res;
    void bt(vector<int> can, int t, int s, int j){
        if(s > t){
            return;
        }
        if(s == t){
            out.push_back(res);
            return;
        }
        for(int i=j; i<can.size(); i++){
            res.push_back(can[i]);
            s += can[i];
            bt(can, t, s, j);
            if(!res.empty()){
                s -= res.back();
                res.pop_back();
            }
            j += 1;
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        bt(candidates, target, 0, 0);
        return out;
    }
};
