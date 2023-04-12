class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # with division!
        # prod = 1
        # zero_count = 0
        # for n in nums:
        #     if n:
        #         prod *= n
        #     else:
        #         zero_count += 1
        # if zero_count == 0:
        #     return [ prod//n for n in nums ]
        # elif zero_count == 1:
        #     return [ 0 if n else prod for n in nums ]
        # else:
        #     return [0]*len(nums)
        out = [1]*len(nums)
        mul = 1
        for i in range(len(nums)-1):
            mul *= nums[i]
            out[i+1] *= mul
        mul = 1
        for i in range(len(nums)-1, 0, -1):
            mul *= nums[i]
            out[i-1] *= mul
        return out
