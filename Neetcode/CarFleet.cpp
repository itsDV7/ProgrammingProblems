class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<int, int> pindex;
        int sz = position.size()-1;
        for (int i=0; i<position.size(); i++){
            pindex[position[i]] = i;
        }
        sort(position.begin(), position.end());
        int fleets = 1;
        stack<int> pstack;
        for (int i=0; i<sz; i++){
            // cout << i << " " << sz - i << " " << sz - (i+1) << "\n";
            // cout << i << " " << speed[pindex[position[sz - i]]] << " " << speed[pindex[position[sz - (i+1)]]] << "\n";
            if (pstack.empty()){
                pstack.push(position[sz - i]);
            }
            // cout << pstack.top() << " " << position[sz - (i+1)] << " ";
            if (speed[pindex[pstack.top()]] >= speed[pindex[position[sz - (i+1)]]]){
                fleets += 1;
                pstack.pop();
                pstack.push(position[sz - (i+1)]);
                // cout << "Front fast!\n";
            }
            else{
                // if ((target-position[i])/speed[pindex[position[i]]] > (target-position[i+1])/speed[pindex[position[i+1]]]){
                //     fleets += 1;
                // }
                float T;
                T = static_cast<float>(pstack.top() - position[sz - (i+1)]) / static_cast<float>(speed[pindex[position[sz - (i+1)]]] - speed[pindex[pstack.top()]]);
                // cout << T << " " << ((target - pstack.top()) / speed[pindex[pstack.top()]]) << "\n";
                if (T > (static_cast<float>(target - pstack.top()) / static_cast<float>(speed[pindex[pstack.top()]]))){
                    fleets += 1;
                    pstack.pop();
                    pstack.push(position[sz - (i+1)]);
                }
                else{
                    speed[pindex[position[sz - (i+1)]]] = speed[pindex[pstack.top()]];
                }
            }
        }
        return fleets;
    }
};
