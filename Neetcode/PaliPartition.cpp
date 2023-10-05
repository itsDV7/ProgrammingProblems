class Solution {
public:
    vector<vector<string>> out;
    vector<string> res;
    bool pali(string s, int i, int j){
        while (i < j){
            if (s[i] != s[j]){
                return false;
            }
            i += 1;
            j -= 1;
        }
        return true;
    }
    void bt(string s, int i){
        if (i >= s.size()){
            out.push_back(res);
            return;
        }
        for(int j=i; j<s.size(); j++){
            if (pali(s, i, j)){
                res.push_back(s.substr(i, j-i+1));
                bt(s, j+1);
                res.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        bt(s, 0);
        return out;
    }
};
