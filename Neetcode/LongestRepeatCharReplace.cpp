#include <unordered_map>
using std::unordered_map;
class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> hashmap;
        int left = 0;
        int right = 0;
        int len = 0;
        while (right < s.length()){
            hashmap[s[right]] += 1;
            int maxfreq = 0;
            for (auto i: hashmap){
                maxfreq = max(maxfreq, i.second);
            }
            if (right - left + 1 - maxfreq <= k){
                len = max(right - left + 1, len);
            }
            else{
                while (right - left + 1 - maxfreq > k){
                    hashmap[s[left]] -= 1;
                    left += 1;
                }
            }
            right += 1;
        }
        return len;
    }
};
