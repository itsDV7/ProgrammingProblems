class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        int s = 0;
        while (i<j){
            s = numbers[i] + numbers[j];
            if (s == target){
                return {i+1, j+1};
            }
            else if (s < target){
                i += 1;
            }
            else{
                j -= 1;
            }
        }
        return {-1, -1};
    }
};
