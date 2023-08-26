class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # SLOWER
        # output = set()
        # res = []
        # index = []
        # def bt():
        #     if len(res) >= len(nums):
        #         output.add(tuple(res))
        #         return
        #     for i in range(len(nums)):
        #         if i not in index:
        #             index.append(i)
        #             res.append(nums[i])
        #             bt()
        #             res.pop()
        #             index.pop()
        # bt()
        # return list(output)

        # FASTER
        op = []
        count = Counter(nums)
        def bt(res, count):
            if len(res) == len(nums):
                op.append(res.copy())
                return
            for n in count:
                if count[n] > 0:
                    res.append(n)
                    count[n] -= 1
                    bt(res, count)
                    count[res.pop()] += 1
        bt([], count)
        return op
