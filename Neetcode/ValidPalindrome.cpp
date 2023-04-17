#include <cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> sv;
        for(char c: s){
            c = tolower(c);
            if (('a' <= c && c <= 'z') || ('0' <= c && c <= '9')){
                sv.push_back(c);
            }
        }
        int i=0;
        int j=sv.size()-1;
        while (i < j){
            if (sv[i] != sv[j]){
                return false;
            }
            i += 1;
            j -= 1;
        }
        return true;
    }
};
