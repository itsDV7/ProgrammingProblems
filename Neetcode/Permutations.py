class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        res = []
        def bt():
            if len(res) >= len(nums):
                output.append(res.copy())
                return
            for n in nums:
                if n not in res:
                    res.append(n)
                    bt()
                    res.pop()
        bt()
        return output
