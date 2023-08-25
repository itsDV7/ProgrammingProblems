class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = set()
        res = []
        index = []
        def bt():
            if len(res) >= len(nums):
                output.add(tuple(res))
                return
            for i in range(len(nums)):
                if i not in index:
                    index.append(i)
                    res.append(nums[i])
                    bt()
                    res.pop()
                    index.pop()
        bt()
        return list(output)
