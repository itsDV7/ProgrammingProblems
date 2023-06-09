class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = 0;
        while (left <= right){
            mid = left + (right - left)/2;
            if (left == right){
                break;
            }
            cout << mid;
            if (nums[mid] > nums[right]){
                left = mid + 1;
            }
            else if (nums[mid] < nums[right]){
                right = mid;
            }
        }
        return nums[mid];
    }
};
