class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = 0;
        while (left <= right){
            if (nums[left] == target){
                return left;
            }
            if (nums[right] == target){
                return right;
            }
            mid = left + (right - left)/2;
            if (nums[mid] == target){
                return mid;
            }
            if (target > nums[mid]){
                if (target > nums[right]){
                    if (nums[mid] > nums[right]){
                        left = mid + 1;
                    }
                    else{
                        right = mid - 1;
                    }
                }
                else{
                    left = mid + 1;
                }
            }
            else{
                if (target < nums[left]){
                    if (nums[mid] > nums[left]){
                        left = mid + 1;
                    }
                    else{
                        right = mid - 1;
                    }
                }
                else{
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};
