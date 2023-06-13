#include <unordered_map>
using std::unordered_map;
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> hashmap;
        int match = s1.length();
        for (char s : s1){
            hashmap[s] += 1;
        }
        int left = 0;
        int right = 0;
        while (right < s2.length()){
            if (hashmap.find(s2[right]) != hashmap.end()){
                if (hashmap[s2[right]]){
                    match -= 1;
                    hashmap[s2[right]] -= 1;
                }
                else{
                    while (s2[left] != s2[right]){
                        if (hashmap.find(s2[left]) != hashmap.end()){
                            hashmap[s2[left]] += 1;
                            match += 1;
                        }
                        left += 1;
                    }
                    left += 1;
                }
            }
            if (match == 0){
                return true;
            }
            if (right - left + 1 < s1.length()){
                right += 1;
            }
            else{
                if (hashmap.find(s2[left]) != hashmap.end()){
                    hashmap[s2[left]] += 1;
                    match += 1;
                }
                left += 1;
                right += 1;
            }
        }
        if (match){
            return false;
        }
        else{
            return true;
        }
    }
};
