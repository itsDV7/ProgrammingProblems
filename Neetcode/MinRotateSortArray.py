class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minelem = 5001
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            mid = left + (right - left)//2
            minelem = min(minelem, nums[mid])
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return minelem
