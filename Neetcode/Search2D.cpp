class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int top = 0;
        int bottom = matrix.size() - 1;
        int mid = -1;
        while (top <= bottom){
            mid = top + (bottom - top)/2;
            if (matrix[mid][0] > target){
                bottom = mid - 1;
            }
            else if (matrix[mid][matrix[mid].size() - 1] < target){
                top = mid + 1;
            }
            else{
                break;
            }
        }
        
        if (top > bottom){
            return false;
        }

        int left = 0;
        int right = matrix[mid].size() - 1;
        while (left <= right){
            int middle = left + (right - left)/2;
            if (matrix[mid][middle] == target){
                return true;
            }
            else if (matrix[mid][middle] < target){
                left = middle + 1;
            }
            else if (matrix[mid][middle] > target){
                right = middle - 1;
            }
        }
        
        return false;
    }
};
