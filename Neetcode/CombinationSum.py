class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # SLOWEST
        # output = set()
        # res = list()
        # def bt(curr_sum):
        #     if curr_sum == target:
        #         output.add(tuple(sorted(res.copy())))
        #         return
        #     if curr_sum > target:
        #         return
        #     for c in candidates:
        #         print(c)
        #         res.append(c)
        #         curr_sum += c
        #         bt(curr_sum)
        #         curr_sum -= res.pop()
        # bt(0)
        # return output

        # FASTER
        # op = []
        # res = []
        # cs = 0
        # candidates.sort()
        # def bt(cs):
        #     if cs == target:
        #         op.append(res.copy())
        #         return False
        #     if cs > target:
        #         return False
        #     for c in candidates:
        #         if res and c < res[-1]:
        #             continue
        #         res.append(c)
        #         cs += c
        #         if not bt(cs):
        #             if res:
        #                 cs -= res.pop()
        #             return True
        #         if res:
        #             cs -= res.pop()
        #     else:
        #         return True
        # bt(0)
        # return op

        # LESS CODE SAME TIME
        op = []
        def bt(i, res, cs):
            if cs == target:
                op.append(res.copy())
                return
            if i >= len(candidates) or cs > target:
                return
            res.append(candidates[i])
            bt(i, res, cs+candidates[i])
            res.pop()
            bt(i+1, res, cs)
        bt(0, [], 0)
        return op
