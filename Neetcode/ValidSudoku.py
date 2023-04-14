class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            cnt = set()
            for v in r:
                if v != ".":
                    if v in cnt:
                        return False
                    cnt.add(v)
        for i in range(len(board)):
            cnt = set()
            for c in board:
                if c[i] != ".":
                    if c[i] in cnt:
                        return False
                    cnt.add(c[i])
        row = 0
        col = 0
        for _ in range(9):
            cnt = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] != ".":
                        if board[i][j] in cnt:
                            return False
                        cnt.add(board[i][j])
            if row == 6:
                row = 0
                col += 3
            else:
                row += 3
        return True
            
