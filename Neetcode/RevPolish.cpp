class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        int r, l;
        for(string c: tokens){
            if (c == "+"){
                r = s.top();
                s.pop();
                l = s.top();
                s.pop();
                s.push(l + r);
            }
            else if (c == "-"){
                r = s.top();
                s.pop();
                l = s.top();
                s.pop();
                s.push(l - r);
            }
            else if (c == "*"){
                r = s.top();
                s.pop();
                l = s.top();
                s.pop();
                s.push(l * r);
            }
            else if (c == "/"){
                r = s.top();
                s.pop();
                l = s.top();
                s.pop();
                s.push(l / r);
            }
            else{
                s.push(stoi(c));
            }
        }
        return s.top();
    }
};
