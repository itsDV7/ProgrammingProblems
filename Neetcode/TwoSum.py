class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if n <= abs(target) and ((target - n) in nums):
                if nums.index(target - n) != i:
                    return [i, nums.index(target - n)]
