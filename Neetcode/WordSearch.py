class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(res, r, c, v):
            if res == word:
                return True
            elif len(res) > len(word):
                return False
            if 0 <= c-1 < len(board[0]) and 0 <= r < len(board) and board[r][c-1] == word[len(res)] and not visited[r][c-1]:
                visited[r][c-1] = True
                if dfs(res+board[r][c-1], r, c-1, visited):
                    return True
                visited[r][c-1] = False
            if 0 <= c < len(board[0]) and 0 <= r+1 < len(board) and board[r+1][c] == word[len(res)] and not visited[r+1][c]:
                visited[r+1][c] = True
                if dfs(res+board[r+1][c], r+1, c, visited):
                    return True
                visited[r+1][c] = False
            if 0 <= c+1 < len(board[0]) and 0 <= r < len(board) and board[r][c+1] == word[len(res)] and not visited[r][c+1]:
                visited[r][c+1] = True
                if dfs(res+board[r][c+1], r, c+1, visited):
                    return True
                visited[r][c+1] = False
            if 0 <= c < len(board[0]) and 0 <= r-1 < len(board) and board[r-1][c] == word[len(res)] and not visited[r-1][c]:
                visited[r-1][c] = True
                if dfs(res+board[r-1][c], r-1, c, visited):
                    return True
                visited[r-1][c] = False
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited = [[False]*len(board[0]) for _ in range(len(board))]
                    visited[r][c] = True
                    if dfs(board[r][c], r, c, visited):
                        return True
        return False
