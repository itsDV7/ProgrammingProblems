class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        res = []
        def pali(st):
            i = 0
            j = len(st)-1
            while i <= j:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1
            return True
        def bt(i):
            if i >= len(s):
                out.append(res.copy())
                return
            for j in range(i, len(s)):
                if pali(s[i:j+1]):
                    res.append(s[i:j+1])
                    bt(j+1)
                    res.pop()
        bt(0)
        return out
