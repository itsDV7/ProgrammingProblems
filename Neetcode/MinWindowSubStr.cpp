#include <unordered_map>
using std::unordered_map;
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> hashmap;
        for (char c : t){
            hashmap[c] += 1;
        }
        int left = 0;
        while (hashmap.find(s[left]) == hashmap.end() && left < s.length()){
            left += 1;
        }
        int right = left;
        int match = hashmap.size();
        int len = s.length() + 1;
        string str = "";
        int minleft = 0;
        int minright = -1;
        while (right < s.length()){
            if (hashmap.find(s[right]) != hashmap.end()){
                hashmap[s[right]] -= 1;
                if (hashmap[s[right]] == 0){
                    match -= 1;
                }
            }
            while (match == 0){
                if (right - left + 1 <= len){
                    // str = s.substr(left, right - left + 1);
                    minleft = left;
                    minright = right;
                    len = right - left + 1;
                }
                if (hashmap[s[left]] == 0){
                    match += 1;
                }
                hashmap[s[left]] += 1;
                left += 1;
                while (hashmap.find(s[left]) == hashmap.end() && left < s.length()){
                    left += 1;
                }
            }
            right += 1;
        }
        str = s.substr(minleft, minright - minleft + 1);
        return str;
    }
};
