class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> temp, index;
        vector<int> ans(temperatures.size());
        for (int i=0; i<temperatures.size(); i++){
            if (temp.empty()){
                temp.push(temperatures[i]);
                index.push(i);
            }
            else{
                if (temperatures[i] <= temp.top()){
                    temp.push(temperatures[i]);
                    index.push(i);
                }
                else{
                    while (!temp.empty() && temperatures[i] > temp.top()){
                        temp.pop();
                        ans[index.top()] = i - index.top();
                        index.pop();
                    }
                    temp.push(temperatures[i]);
                    index.push(i);
                }
            }
        }
        return ans;
    }
};
