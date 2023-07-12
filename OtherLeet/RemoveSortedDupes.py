class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        swaps = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            elif right - left > 1:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
                swaps += 1
            else:
                left += 1
                swaps += 1
        return swaps + 1
            
