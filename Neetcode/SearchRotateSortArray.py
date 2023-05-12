class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        else:
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                if nums[mid] < nums[right]:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if nums[right] < target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1
