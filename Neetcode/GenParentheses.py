class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def bt(O, N):
            if O == N == n:
                res.append(''.join(stack))
                return
            if O < n:
                stack.append("(")
                bt(O+1, N)
                stack.pop()
            if N < O:
                stack.append(")")
                bt(O, N+1)
                stack.pop()
        bt(0, 0)
        return res    
