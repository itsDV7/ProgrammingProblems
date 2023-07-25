class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr or len(arr) < 3:
            return -1
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left)//2
            mid_val = arr[mid]
            mid_left_val = arr[mid-1] if mid - 1 >= 0 else -1
            mid_right_val = arr[mid+1] if mid + 1 < len(arr) else -1
            if mid_left_val < mid_val > mid_right_val:
                return mid
            elif mid_left_val > mid_val:
                right = mid - 1
            else:
                left = mid + 1
        return -2
