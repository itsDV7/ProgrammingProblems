#include <unordered_map>
using std::unordered_map;
class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> dict;
    TimeMap() {

    }
    
    void set(string key, string value, int timestamp) {
        dict[key].push_back(make_pair(value, timestamp));
    }
    
    string get(string key, int timestamp) {
        if (dict.find(key) == dict.end()){
            return "";
        }
        else{
            int left = 0;
            int right = dict[key].size() - 1;
            int mid = 0;
            while (left <= right){
                mid = left + (right - left)/2;
                // cout << mid << " " << dict[key][mid].first << " " << dict[key][mid].second << "\n";
                if (dict[key][mid].second == timestamp){
                    return dict[key][mid].first;
                }
                if (dict[key][mid].second < timestamp){
                    left = mid + 1;
                }
                else{
                    right = mid - 1;
                }
            }
            while (mid >= 0){
                if (dict[key][mid].second <= timestamp){
                    return dict[key][mid].first;
                }
                mid -= 1;
            }
            return "";
        }
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
