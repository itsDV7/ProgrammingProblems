class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        op = []
        def bt(i, res, cs):
            if cs == target:
                op.append(res[::])
                return
            if i >= len(candidates) or cs > target:
                return
            res.append(candidates[i])
            bt(i+1, res, cs+candidates[i])
            res.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            bt(i+1, res, cs)
        bt(0, [], 0)
        return op
