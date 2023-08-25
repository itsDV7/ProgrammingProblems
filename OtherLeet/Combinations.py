class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        res = []
        def bt(i, l):
            # print(i, l)
            if i > n:
                return
            if l == k:
                output.append(res.copy())
                return
            res.append(i+1)
            l += 1
            bt(i+1, l)
            res.pop()
            l -= 1
            bt(i+1, l)
        bt(0, 0)
        return output
