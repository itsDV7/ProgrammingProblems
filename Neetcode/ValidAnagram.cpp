class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> s_count, t_count;
        if (s.length() != t.length()){
            return false;
        }
        else{
            for (int i = 0; i < s.length(); i++){
                if (s_count.find(s[i]) != s_count.end()){
                    s_count[s[i]] += 1;
                }
                else{
                    s_count[s[i]] = 1;
                }
                if (t_count.find(t[i]) != t_count.end()){
                    t_count[t[i]] += 1;
                }
                else{
                    t_count[t[i]] = 1;
                }
            }
            for (auto pair: s_count){
                if (t_count.find(pair.first) == t_count.end()){
                    return false;
                }
                else if (t_count[pair.first] != pair.second){
                    return false;
                }
            }
            return true;
        }
    }
};
