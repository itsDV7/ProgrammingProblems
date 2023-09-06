class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        elif n <= 3:
            return None
        else:
            out = []
            place = [["."]*n for _ in range(n)]
            cols = set()
            posiDiag = set()
            negiDiag = set()
            def bt(i):
                if i >= n:
                    out.append([''.join(r.copy()) for r in place.copy()])
                    return
                
                for j in range(n):
                    if j in cols or (j-i) in negiDiag or (j+i) in posiDiag:
                        continue
                    cols.add(j)
                    posiDiag.add(j+i)
                    negiDiag.add(j-i)
                    place[i][j] = "Q"
                    bt(i+1)
                    place[i][j] = "."
                    cols.remove(j)
                    posiDiag.remove(j+i)
                    negiDiag.remove(j-i)
            
            bt(0)
            return out
