#include <map>
#include <string>


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> vect;
        map<map<char, int>, vector<string>> ans;
        for(string s: strs){
            map<char, int> count;
            for(char c: s){
                if (count.find(c) != count.end()){
                    count[c] += 1;
                }
                else{
                    count[c] = 1;
                }
            }
            ans[count].push_back(s);
        }
        for (auto itr=ans.begin(); itr!=ans.end(); itr++){
            vect.push_back(itr->second);
        }
        return vect;
    }
};
