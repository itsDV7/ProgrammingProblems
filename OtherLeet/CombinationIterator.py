class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.op = self.bt(list(characters), combinationLength, [])
        self.iter = 0

    def bt(self, chars, n, op):
        def dfs(i, res):
            if len(res) == n:
                op.append(''.join(res))
                return
            if i >= len(chars) or len(res) > n:
                return
            res.append(chars[i])
            dfs(i+1, res)
            res.pop()
            dfs(i+1, res)
        dfs(0, [])
        return op

    def next(self) -> str:
        self.iter += 1
        return self.op[self.iter-1]

    def hasNext(self) -> bool:
        if self.iter < len(self.op):
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
