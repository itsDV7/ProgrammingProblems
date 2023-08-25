class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        op = list()
        def bt(i, res, cs):
            if len(res) == k and cs == n:
                op.append(res.copy())
                return
            if len(res) > k or cs > n or i >= 9:
                return
            res.append(i+1)
            bt(i+1, res, cs+i+1)
            res.pop()
            bt(i+1, res, cs)
        bt(0, [], 0)
        return op
