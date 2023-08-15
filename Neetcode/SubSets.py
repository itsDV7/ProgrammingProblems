class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        res = []
        def bt(i):
            if i >= len(nums):
                output.append(res.copy())
                return
            res.append(nums[i])
            bt(i + 1)
            res.pop()
            bt(i + 1)
        bt(0)
        return output
