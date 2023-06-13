#include <unordered_set>
using std::unordered_set;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        cout << s.length();
        int left = 0;
        int maxlen = 0;
        int i=0;
        unordered_set<char> hashset;
        for (; i<s.length(); i++){
            if (hashset.find(s[i]) != hashset.end()){
                maxlen = max(maxlen, i-left);
                while (s[left] != s[i]){
                    hashset.erase(s[left]);
                    left += 1;
                }
                left += 1;
            }
            else{
                hashset.insert(s[i]);
            }
        }
        cout << left << i;
        maxlen = max(maxlen, i-left);
        return maxlen;
    }
};
