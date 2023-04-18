class Solution {
public:
    vector<string> ans;
    vector<string> generateParenthesis(int n) {
        stack<char> s;
        X(s, n, n);
        return ans;
    }
    void X(stack<char> s, int o, int c){
        // if (s.empty() && o>0){
        //     s.push('(');
        //     X(s, o-1, c);
        //     s.pop();
        // }
        if (o>0){
            s.push('(');
            X(s, o-1, c);
            s.pop();
        }
        if (c>0 && o<c){
            s.push(')');
            X(s, o, c-1);
            s.pop();
        }
        if (c==0 && o==0){
            // int sz = s.size();
            string ans_s("");
            stack<char> rs;
            while(!s.empty()){
                rs.push(s.top());
                s.pop();
            }
            while(!rs.empty()){
                // cout << rs.top();
                ans_s += rs.top();
                rs.pop();
            }
            // cout << ans_s;
            ans.push_back(ans_s);
            // cout << "\n";
        }
    }
};
