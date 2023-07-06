class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        minlen = len(nums) + 1
        currsum = 0
        while right < len(nums):
            currsum += nums[right]
            while currsum >= target:
                minlen = min(minlen, right-left+1)
                currsum -= nums[left]
                left += 1
            right += 1
        return minlen if minlen < len(nums) + 1 else 0
