class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left = -1;
        int right = -1;
        int mid = -1;
        for (int i=0; i < matrix.size(); i++){
            left = 0;
            right = matrix[i].size() - 1;
            if (matrix[i][left] > target){
                return false;
            }
            while (left <= right){
                mid = left + (right - left)/2;
                if (matrix[i][mid] == target){
                    return true;
                }
                else if (matrix[i][mid] < target){
                    left = mid + 1;
                }
                else if (matrix[i][mid] > target){
                    right = mid - 1;
                }
            }
        }
        return false;
    }
};
